<template>
  <div class="container" style="padding-top:50px">
    <div v-if="!this.$store.getters.isLoggedIn">
      <i class="fas fa-question major-icon"></i>
      <!-- <h3 class="mt-4 mb-2">You are not logged in</h3> -->
      <p class="my-4">
        <router-link class="mx-1" to="/login">Log in</router-link>to see projects only in your major!
      </p>
    </div>
    <!-- major icon -->
    <div v-if="this.$store.getters.isLoggedIn">
      <i class="fas fa-laptop-code major-icon" v-if="$store.getters.getUserMajor === 'CSE'"></i>
      <i class="fas fa-user-tie major-icon" v-if="$store.getters.getUserMajor === 'Business'"></i>
      <i class="fas fa-user-md major-icon" v-if="$store.getters.getUserMajor === 'Medical'"></i>
      <i class="fas fa-book major-icon" v-if="$store.getters.getUserMajor === 'Literature'"></i>
    </div>

    <div class="w-50 my-4 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div>

    <div class="row">
      <div class="col-lg-7 col-md-12 my-4" style="height:500px">
        <ProjectList
          :projects="projects.length>0 ? filterProjects(projects) : []"
          @clickProject="clickProject"
        />
      </div>
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
      chosenProject: {}
    };
  },
  methods: {
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    },
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
    if (this.$store.getters.isLoggedIn) {
      major = this.$store.getters.getUserMajor;
    }
    this.$axios
      .get("/api/projects/", { params: { major: major } })
      .then(response => {
        this.projects = response.data;
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
  color: #7ecfc0;
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
