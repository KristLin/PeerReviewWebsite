<template>
  <div class="container">
    <div class="card mx-auto shadow creat-project-form">
      <div class="card-header">Create a new project</div>
      <div class="card-body">
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            v-model="projectData.title"
            placeholder="Project Title"
          />
        </div>

        <div class="form-group">
          <textarea
            class="form-control"
            v-model="projectData.description"
            cols="30"
            rows="5"
            placeholder="Project description"
          ></textarea>
        </div>

        <!-- input files -->
        <input
          type="file"
          style="display: none"
          accept=".txt"
          ref="filesInput"
          @change="selectFiles"
          multiple
        />
        <button class="my-btn form-control" @click="$refs.filesInput.click()">Select Files</button>
        <!-- input files end -->

        <!-- files display -->
        <div class="card my-4">
          <div class="card-header">Project Files</div>
          <div class="card-body">
            <p
              class="card-text text-left"
              :key="idx"
              v-for="(file, idx) in projectData.files"
            >{{ file.name }}</p>
          </div>
        </div>
        <!-- files display end -->

        <div class="form-group">
          <button class="my-btn form-control" @click="createProject">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "createProject",
  data() {
    return {
      projectData: {
        title: "",
        description: "",
        files: []
      }
    };
  },
  components: {},
  methods: {
    createProject() {
      // get local time in the format: "dd/mm/yyyy, hh:mm:ss"
      // this.projectData.createdTime = new Date().toLocaleString("en-GB");

      // compare two time
      // let newTime = '02/11/2019, 17:30:57'
      // window.console.log(newtime > this.projectData.createdTime)
      for (let key in this.projectData) {
        if (this.projectData[key].length === 0) {
          this.$swal(
            "Warning",
            "The project upload form is not complete! (" + key + ")",
            "warning"
          );
          return;
        }
      }
      this.projectData.user = this.$store.getters.getUserId;
      this.projectData.major = this.$store.getters.getUserMajor;

      window.console.log("project data before upload:", this.projectData);
      this.$axios
        .post("/api/projects/", this.projectData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.$swal("Success", "You has created a new project!", "success");
            this.$router.push({
              name: "myProjects"
            });
          }
        })
        .catch(err => {
          window.console.log(err.response);
          this.$swal(
            "Oops",
            "Something is wrong, please try again later...",
            "error"
          );
          this.$router.push({
            name: "myProject"
          });
        });
    },

    // read file text content
    getFileContent(file, callback) {
      var reader = new FileReader();

      reader.onload = function(event) {
        callback(event.target.result);
      };
      reader.readAsText(file, "UTF-8");
    },

    // handle select files
    selectFiles(event) {
      let fileList = Array.from(event.target.files);
      if (fileList) {
        for (let key in fileList) {
          let fileName = fileList[key].name;
          window.console.log("file name:", fileName);

          this.getFileContent(fileList[key], fileContent => {
            this.projectData.files.push({
              name: fileName,
              content: fileContent,
              mark: 0
            });
          });
        }
      }
    }
  },
  created() {
    if (!this.$store.getters.isLoggedIn) {
      this.$swal("Error", "Log in required!", "error");
      window.console.log("need user login");
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
.creat-project-form {
  width: 500px;
}
</style>
