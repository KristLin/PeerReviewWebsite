<template>
  <div class="container" style="padding-top:50px">
    <div class="card mx-auto shadow creat-project-form">
      <div class="card-header">Create a new project</div>
      <div class="card-body">
        <!-- project title input start -->
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            v-model="projectData.title"
            placeholder="Project Title"
          />
        </div>
        <!-- project title input end -->

        <!-- project description input start -->
        <div class="form-group">
          <textarea
            class="form-control"
            v-model="projectData.description"
            cols="30"
            rows="5"
            placeholder="Project description"
          ></textarea>
        </div>
        <!-- project description input end -->

        <!-- project files input start -->
        <!-- hidden files input -->
        <input
          type="file"
          style="display: none"
          accept=".txt, .html, .css, .py, .js"
          ref="filesInput"
          @change="selectFiles"
          multiple
        />
        <!-- button to call the files input -->
        <button class="my-btn form-control" @click="$refs.filesInput.click()">Select Files</button>
        <!-- project files input end -->

        <!-- files display -->
        <div class="card my-4">
          <div class="card-header">Project Files</div>
          <div class="card-body">
            <!-- display all files of the project -->
            <div
              class="file-row text-left"
              :key="idx"
              v-for="(file, idx) in projectData.files"
            >{{ file.name }}</div>
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
      // ===== following code is used for testing date format =====
      // get local time in the format: "dd/mm/yyyy, hh:mm:ss"
      // this.projectData.createdTime = new Date().toLocaleString("en-GB");

      // compare two time
      // let newTime = '02/11/2019, 17:30:57'
      // window.console.log(newtime > this.projectData.createdTime)
      // ===================== test code end =====================

      // check if all inputs have filled in
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
      // add user ID and user major to the projectData as properties "user" and "major"
      this.projectData.user = this.$store.getters.getUserId;
      this.projectData.major = this.$store.getters.getUserMajor;

      window.console.log("project data before upload:", this.projectData);
      // post projectData to backend to create the project
      this.$axios
        .post("/api/projects/", this.projectData)
        .then(response => {
          if (response.status == 200) {
            this.$swal("Success", "You has created a new project!", "success");
            this.$router.push({
              name: "myProjects"
            });
          }
        })
        // notify user when there is an error
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
      this.projectData.files = [];
      // transform files in the input to an files array
      let fileList = Array.from(event.target.files);
      if (fileList) {
        for (let key in fileList) {
          let fileName = fileList[key].name;
          window.console.log("file name:", fileName);

          // form a file object using current file's data,
          // and push it to projectData's files property
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
    // if the user is not logged in, send the user to login page
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

@media screen and (max-width: 625px) {
  .creat-project-form {
    width: 100%;
  }
}

.file-row:hover {
  background-color: rgba(0, 0, 0, 0.03);
}
</style>
