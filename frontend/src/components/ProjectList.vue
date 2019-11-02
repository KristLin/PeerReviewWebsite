<template>
  <div class="project-list overflow-auto" style="height: 500px;">
    <div
      class="card mb-4"
      @click="clickProject(project)"
      :key="idx"
      v-for="(project, idx) in projects"
    >
      <div class="card-header my-bg font-weight-bold">{{ project.name }}</div>
      <div class="card-body">
        <p>{{ project.description }}</p>
      </div>
      <div class="card-footer p-1">
        <small>{{ project.createdTime }}</small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectList",
  props: {
    projects: Array
  },
  methods: {
    clickProject(project) {
      window.console.log("clicked project in ProjectList", project)
      this.$emit("clickProject", project);
    }
  }
};
</script>

<style scoped>
</style> 