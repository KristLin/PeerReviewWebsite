<template>
  <div style="height: 500px;">
    <!-- project info dispaly -->
    <div class="project-info overflow-auto" v-if="project.name">
      <div class="card mb-4">
        <div class="card-header my-bg">{{ project.name }}</div>
        <div class="card-body">
          <p>{{ project.description }}</p>
        </div>
        <div class="card mx-4 my-4">
          <div class="card-header">File List:</div>
          <div class="card-body text-left">
            <p
              class="file-name"
              @click="clickFile(file)"
              :key="idx"
              v-for="(file, idx) in project.files"
            >{{ file.name }}</p>
          </div>
        </div>
        <div class="card-footer p-1">
          <small>{{ project.createdTime }}</small>
        </div>
      </div>
    </div>
    <!-- project info dispaly end -->

    <!-- hint -->
    <div v-if="!project.name">
      <p style="padding-top: 200px">Click a project to see more.</p>
    </div>
    <!-- hint end -->
  </div>
</template>

<script>
export default {
  name: "ProjectList",
  props: {
    project: Object
  },
  methods: {
    clickFile(file) {
      window.console.log("clicked file in ProjectInfo", file);
      this.$router.push({
        name: "file",
        query: { fileId: file.id },
        params: { file: file }
      });
    }
  }
};
</script>

<style scoped>
.file-name:hover {
  color: #9852f9;
}
</style> 