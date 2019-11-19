<template>
  <div class="container" style="padding-top:50px">
    <!-- show question icon when user is not logged in  -->
    <div v-if="!this.$store.getters.isLoggedIn">
      <i class="fas fa-question major-icon"></i>
      <p class="my-4">
        <router-link class="mx-1" to="/login">Log in</router-link>to see projects only in your major!
      </p>
    </div>

    <!-- major icon -->
    <div v-if="this.$store.getters.isLoggedIn">
      <i class="fas fa-laptop-code major-icon" v-if="$store.getters.getUserMajor === 'CSE'"></i>
      <i class="fas fa-user-tie major-icon" v-if="$store.getters.getUserMajor === 'Business'"></i>
      <i class="fas fa-stethoscope major-icon" v-if="$store.getters.getUserMajor === 'Medical'"></i>
      <i class="fas fa-book major-icon" v-if="$store.getters.getUserMajor === 'Literature'"></i>
    </div>

    <!-- keyword input -->
    <div class="w-50 my-4 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div>

    <div class="row">
      <!-- Loading animation-->
      <div class="col-lg-7 col-md-12 my-4" style="padding-top: 100px" v-if="!hasFetchedData">
        <h4 class="my-4">Loading ...</h4>
        <b-spinner variant="secondary" style="width: 5rem; height: 5rem; font-size:2rem;" label="Loading..."></b-spinner>
      </div>

      <!-- project list component -->
      <div class="col-lg-7 col-md-12 my-4" style="height:500px" v-if="hasFetchedData">
        <ProjectList
          :projects="projects.length>0 ? filterProjects(projects) : []"
          @clickProject="clickProject"
        />
      </div>

      <!-- project info component -->
      <div class="col-lg-5 col-md-12 my-4" style="height:500px">
        <ProjectInfo :project="chosenProject" />
      </div>
    </div>
  </div>
</template>

<script>
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "search",
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
      chosenProject: {},
      hasFetchedData: false
    };
  },
  methods: {
    // assign the clicked project data to chosenProject
    // so the projectInfo component can render the project information
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    },

    // projects filter function
    // return the project if its title or description contains the keyword
    filterProjects(projects) {
      let keyword = this.searchData.keyword.toLowerCase();
      var filteredProjects = projects.filter(function(project) {
        return (
          project.title.toLowerCase().includes(keyword) ||
          project.description.toLowerCase().includes(keyword)
        );
      });
      return filteredProjects;
    }
  },

  created() {
    var major = "";
    // get user major if logged in
    if (this.$store.getters.isLoggedIn) {
      major = this.$store.getters.getUserMajor;
    }
    // request projects data from backend
    this.$axios
      .get("/api/projects/", { params: { major: major } })
      .then(response => {
        this.projects = response.data;
        this.hasFetchedData = true
      })
      .catch(err => {
        window.console.log(err.response);
      });
  }
};
</script>

<style scoped>
.major-icon {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  color: #6fc4b4;
  line-height: 100px;
  text-align: center;
  background: rgba(180, 175, 175, 0.25);
  font-weight: bold;
  font-size: 2.5rem;
}

.major-icon:hover {
  color: #6bafa3;
}
</style>
