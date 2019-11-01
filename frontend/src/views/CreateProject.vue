<template>
  <div class="container creat-project-form">
    <div class="card shadow">
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

        <div class="card my-4">
          <div class="card-header">Project Files</div>
          <div class="card-body">
            <p
              class="card-text text-left"
              :key="idx"
              v-for="(fileName, idx) in displayData.fileNameList"
            >{{ fileName }}</p>
          </div>
        </div>
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
        owner: this.$store.getters.getUserId,
        major: this.$store.getters.getUserMajor,
        title: "",
        description: "",
        files: [],
        rating: "0",
        rating_num: "0"
      },
      displayData: {
        fileNameList: []
      }
    };
  },
  components: {},
  methods: {
    createProject() {
      window.console.log(this.projectData);
    },
    selectFiles(event) {
      let fileArray = Array.from(event.target.files);
      if (fileArray) {
        var reader = new FileReader();

        for (let key in fileArray) {
          let fileName = fileArray[key].name;
          window.console.log("file name:", fileName);
          reader.readAsText(fileArray[key], "UTF-8");
          this.displayData.fileNameList.push(fileName);
          reader.onload = function() {
            window.console.log("file content:", reader.result);
          };
          this.projectData.files.push({
            name: fileName,
            content: reader.result
          });
        }
      }
    }
  }
};
</script>

<style scoped>
.creat-project-form {
  width: 400px;
  margin-top: 50px;
  margin-bottom: 100px;
}

.my-btn {
  border: none;
  background-color: #c299fc;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #9852f9;
  color: white;
}
</style>
