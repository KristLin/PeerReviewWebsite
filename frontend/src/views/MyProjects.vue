<template>
  <div class="container">
    <h1>My Projects</h1>
    <p class="text-right">Rest Top Times: 10</p>
    <div class="w-50 my-2 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div>

    <button class="my-btn w-50 mx-auto my-4 form-control" @click="createProject">Create New Project</button>
    <hr />

    <div class="row">
      <!-- project list -->
      <div class="col-lg-7 col-md-12 md-4" style="height:500px">
        <ProjectList :projects="projects" @clickProject="clickProject" />
      </div>
      <!-- project list end -->

      <!-- top up button & project info -->
      <div class="col-lg-5 col-md-12 md-4">
        <div class="row" style="height:50px">
          <button
            class="form-control btn btn-warning"
            v-if="chosenProject.title && !chosenProject.isOnTop"
            @click="topUpProject"
          >Top Up!</button>
          <button
            class="form-control btn btn-danger"
            v-if="chosenProject.title && chosenProject.isOnTop"
            @click="cancelTopUp"
          >Cancel Top Up</button>
          <p class="form-control" v-if="!chosenProject.title">Top Up!</p>
        </div>
        <div class="row" style="height:450px">
          <ProjectInfo :project="chosenProject" />
        </div>
      </div>
      <!-- top up button & project info end -->
    </div>
  </div>
</template>

<script>
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "myProjects",
  components: {
    ProjectList,
    ProjectInfo
  },
  data() {
    return {
      searchData: {
        keyword: "",
        orderType: ""
      },
      projects: [],
      chosenProject: {}
    };
  },
  methods: {
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    },
    createProject() {
      this.$router.push({ name: "createProject" });
    },
    topUpProject() {
      window.console.log("Top up request: ", this.chosenProject);
      this.chosenProject.isOnTop = true;
      this.chosenProject.isOnTopTime = new Date().toLocaleString("en-GB");

      this.$axios
        .patch("/api/projects/" + this.chosenProject._id, this.chosenProject)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.$axios
              .get("/api/projects/user/" + this.$store.getters.getUserId)
              .then(response => {
                // JSON responses are automatically parsed.
                if (response.status == 200) {
                  this.projects = response.data;
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
            this.$swal("Success", "Project is topped up!", "success");
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    },
    cancelTopUp() {
      window.console.log("cancel top up request", this.chosenProject);
      this.chosenProject.isOnTop = false;
      this.chosenProject.isOnTopTime = "";

      this.$axios
        .patch("/api/projects/" + this.chosenProject._id, this.chosenProject)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.$axios
              .get("/api/projects/user/" + this.$store.getters.getUserId)
              .then(response => {
                // JSON responses are automatically parsed.
                if (response.status == 200) {
                  this.projects = response.data;
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
            this.$swal("Success", "Project is not topped up now.", "success");
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    if (this.$store.getters.isLoggedIn) {
      this.$axios
        .get("/api/projects/user/" + this.$store.getters.getUserId)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.projects = response.data;
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    } else {
      window.console.log("user is not logged in");
      this.$swal("Error", "Log in required!", "error");
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
</style>
