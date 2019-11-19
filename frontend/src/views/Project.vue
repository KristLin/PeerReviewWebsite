<template>
  <div class="container" style="padding-top:50px">
    <!-- project info component -->
    <div class="mx-auto w-50" style="height:500px; min-width:450px">
      <ProjectInfo :project="project" />
    </div>
  </div>
</template>

<script>
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "project",
  components: { ProjectInfo },
  data() {
    return {
      projectId: this.$route.query.projectId,
      project: this.$route.params.project
    };
  },
  created() {
    window.console.log(
      "received query and param in project vue:",
      this.projectId,
      this.project
    );
    // when the project data (in route params) is lost
    // send request to backend to get the project data
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log("lost route params");
      // this page is not used in the website
      // just for early stage testing
      this.project = {
        id: "1",
        name: "Peer Review Frontend",
        description: "A simple frontend of peer review website",
        major: "CSE",
        createdTime: "2019-10-29 16:00:00",
        files: [
          {
            id: "1",
            name: "index.html",
            content: "<h1>Hello World</h1>\n<h1>Bye World</h1>",
            rating: 3.8
          },
          {
            id: "2",
            name: "index.css",
            content: "h1{\n\tcolor: blue;\n}",
            rating: 3.5
          }
        ]
      };
    }
  }
};
</script>

<style scoped>
</style>
