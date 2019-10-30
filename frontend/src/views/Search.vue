<template>
  <div class="container">
    <SearchInput />
    <hr />
    <div class="row">
      <div class="col-8">
        <ProjectList />
      </div>
      <div class="col-4">
        project Info
      </div>
    </div>
  </div>
</template>

<script>
import SearchInput from "@/components/SearchInput.vue";
import ProjectList from "@/components/ProjectList.vue";

export default {
  name: "search",
  components: {
    SearchInput,
    ProjectList
  }
};
</script>

<style scoped>
</style>
