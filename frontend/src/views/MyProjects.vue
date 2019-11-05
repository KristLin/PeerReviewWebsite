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
          <button class="form-control btn btn-warning" v-if="chosenProject.name">Top Up!</button>
          <p class="form-control" v-if="!chosenProject.name">Top Up!</p>
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
