<template>
  <div class="container">
    <h1>Your Projects</h1>
    <SearchInput />

    <button
      class="my-btn w-50 mx-auto my-4 form-control"
      @click="$router.push({name: 'createProject'})"
    >Create New Project</button>

    <div class="row">
      <div class="col-7">
        <ProjectList />
      </div>
      <div class="col-5">
        <ProjectInfo />
      </div>
    </div>
  </div>
</template>

<script>
import SearchInput from "@/components/SearchInput.vue";
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "myProjects",
  components: {
    SearchInput,
    ProjectList,
    ProjectInfo
  }
};
</script>

<style scoped>
</style>
