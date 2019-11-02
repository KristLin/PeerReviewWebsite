<template>
  <div class="container">
    <div class="w-50 mx-auto">
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
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log("lost route params");
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
            mark: 3.8
          },
          {
            id: "2",
            name: "index.css",
            content: "h1{\n\tcolor: blue;\n}",
            mark: 3.5
          }
        ]
      };
    }
  }
};
</script>

<style scoped>
</style>
