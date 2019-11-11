<template>
  <div class="container" style="padding-top:50px">
    <h1>My Projects</h1>
    <!-- <div class="w-50 my-2 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div> -->

    <button class="my-btn w-50 mx-auto my-4 form-control" @click="createProject">Create New Project</button>
    <hr />

    <div class="row">
      <!-- Loading -->
      <div class="col-lg-7 col-md-12 my-4" style="padding-top: 100px" v-if="!hasFetchedData">
        <h4 class="my-4">Loading ...</h4>
        <b-spinner
          variant="secondary"
          style="width: 5rem; height: 5rem; font-size:2rem;"
          label="Loading..."
        ></b-spinner>
      </div>

      <!-- project list -->
      <div class="col-lg-7 col-md-12 my-4" style="height:500px" v-if="hasFetchedData">
        <ProjectList :projects="projects" @clickProject="clickProject" />
      </div>
      <!-- project list end -->

      <!-- top up button & project info -->
      <div class="col-lg-5 col-md-12 my-4">
        <div style="height:50px">
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

        <div style="height:400px">
          <ProjectInfo :project="chosenProject" />
        </div>

        <div style="margin-top:12px">
          <button
            class="form-control btn btn-danger m-0 p-0"
            v-if="chosenProject.title"
            @click="deleteProject"
          >Delete Project</button>

          <p class="form-control" v-if="!chosenProject.title">Delete Project</p>
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
      // searchData: {
      //   keyword: "",
      //   orderType: ""
      // },
      projects: [],
      chosenProject: {},
      hasFetchedData: false
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
      this.$axios
        .get("/api/projects/topup", {
          params: {
            project_id: this.chosenProject._id,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.chosenProject.isOnTop = true;
            this.chosenProject.isOnTopTime = new Date().toLocaleString("en-GB");
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
          this.$swal("Error", err.response.data, "error");
          window.console.log(err.response);
        });
    },
    cancelTopUp() {
      window.console.log("cancel top up request", this.chosenProject);

      this.$axios
        .get("/api/projects/cancel_topup", {
          params: {
            project_id: this.chosenProject._id,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          if (response.status == 200) {
            this.chosenProject.isOnTop = false;
            this.chosenProject.isOnTopTime = "";
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
          this.$swal("Error", err.response.data, "error");
          window.console.log(err.response);
        });
    },
    deleteProject() {
      this.$swal({
        title: "Confirm",
        text: "Are you sure to delete this project?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Delete"
      }).then(result => {
        if (result.value) {
          this.$axios
            .delete("/api/projects/" + this.chosenProject._id)
            .then(res => {
              if (res.status == 200) {
                // delete project in frontend (so no need to request backend)
                this.projects = this.projects.filter(
                  item => item._id !== this.chosenProject._id
                );
                this.chosenProject = {};

                window.console.log("project is deleted");
                this.$swal("Success", "Project is deleted!", "success");
              }
            })
            .catch(err => window.console.log(err));
        }
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
            this.hasFetchedData = true;
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
