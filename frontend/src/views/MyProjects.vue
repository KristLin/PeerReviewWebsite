<template>
  <div class="container" style="padding-top:50px">
    <h1>My Projects</h1>
    <!-- search input component start -->
    <!-- <div class="w-50 my-2 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div> -->
    <!-- search input component end -->

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

      <!-- project list component start -->
      <div class="col-lg-7 col-md-12 my-4" style="height:500px" v-if="hasFetchedData">
        <ProjectList :projects="projects" @clickProject="clickProject" />
      </div>
      <!-- project list component end -->

      <!-- project display part start -->
      <div class="col-lg-5 col-md-12 my-4">
        <!-- top up/cancel top up buttons start -->
        <div style="height:50px">
          <!-- top up button -->
          <button
            class="form-control btn btn-warning"
            v-if="chosenProject.title && !chosenProject.isOnTop"
            @click="topUpProject"
          >Top Up!</button>

          <!-- cancel top up button -->
          <button
            class="form-control btn btn-danger"
            v-if="chosenProject.title && chosenProject.isOnTop"
            @click="cancelTopUp"
          >Cancel Top Up</button>

          <!-- show text if no project is clicked -->
          <p class="form-control" v-if="!chosenProject.title">Top Up!</p>
        </div>
        <!-- top up/cancel top up buttons end -->

        <!-- project info component -->
        <div style="height:400px">
          <ProjectInfo :project="chosenProject" />
        </div>

        <!-- delete project button -->
        <div style="margin-top:12px">
          <button
            class="form-control btn btn-danger m-0 p-0"
            v-if="chosenProject.title"
            @click="deleteProject"
          >Delete Project</button>
          <p class="form-control" v-if="!chosenProject.title">Delete Project</p>
        </div>
      </div>
      <!-- project display part end -->
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
      // project list
      projects: [],
      // clicked project
      chosenProject: {},
      // all required data has fetched or not
      // to decide when to show loading animation
      hasFetchedData: false
    };
  },
  methods: {
    // assign clicked project data to chosenProject
    // so that the project info component can display the project information
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    },

    // take user to create project page
    createProject() {
      this.$router.push({ name: "createProject" });
    },

    // top up chosen project
    topUpProject() {
      window.console.log("Top up request: ", this.chosenProject);
      // send top up request to backend
      this.$axios
        .get("/api/projects/topup", {
          params: {
            project_id: this.chosenProject._id,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          if (response.status == 200) {
            // update project top up information in frontend side
            this.chosenProject.isOnTop = true;
            this.chosenProject.isOnTopTime = new Date().toLocaleString("en-GB");
            // request updated project list
            this.$axios
              .get("/api/projects/user/" + this.$store.getters.getUserId)
              .then(response => {
                if (response.status == 200) {
                  this.projects = response.data;
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
            // notify user when top up is succeed
            this.$swal("Success", "Project is topped up!", "success");
          }
        })
        // notify user when there is an error
        .catch(err => {
          this.$swal("Error", err.response.data, "error");
          window.console.log(err.response);
        });
    },

    // cancel top up chosen project
    cancelTopUp() {
      window.console.log("cancel top up request", this.chosenProject);
      // send cancel topup request to backend
      this.$axios
        .get("/api/projects/cancel_topup", {
          params: {
            project_id: this.chosenProject._id,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          if (response.status == 200) {
            // update project top up information in frontend side
            this.chosenProject.isOnTop = false;
            this.chosenProject.isOnTopTime = "";
            // request updated project list
            this.$axios
              .get("/api/projects/user/" + this.$store.getters.getUserId)
              .then(response => {
                if (response.status == 200) {
                  this.projects = response.data;
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
            // notify user when cancel top up is succeed
            this.$swal("Success", "Project is not topped up now.", "success");
          }
        })
        // notify user when there is an error
        .catch(err => {
          this.$swal("Error", err.response.data, "error");
          window.console.log(err.response);
        });
    },

    // delete chosen project
    deleteProject() {
      // show a dialog to confirm user's request
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
          // send delete request to backend
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
    // check if user has logged in
    if (this.$store.getters.isLoggedIn) {
      // request user's projects data from backend
      this.$axios
        .get("/api/projects/user/" + this.$store.getters.getUserId)
        .then(response => {
          if (response.status == 200) {
            this.projects = response.data;
            this.hasFetchedData = true;
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    // take user to login page if not logged in yet
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
