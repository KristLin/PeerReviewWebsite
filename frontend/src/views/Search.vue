<template>
  <div class="container">
    <div class="p-4">
      <form action>
        <input type="text" class="form-control" placeholder="Keyword" />
        <button class="btn btn-primary btn-md form-control">Search Project</button>
      </form>
    </div>
    <div class="project-list overflow-auto" style="height: 500px;">
      <div class="card mb-4">
        <div class="card-body">
          <h5 class="card-title">Project Title</h5>
          <p>Project Description</p>
        </div>
        <div class="card-footer">
          <small>Rating: 4.0</small>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body">
          <h5 class="card-title">Project Title</h5>
          <p>Project Description</p>
        </div>
        <div class="card-footer">
          <small>Rating: 4.0</small>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body">
          <h5 class="card-title">Project Title</h5>
          <p>Project Description</p>
        </div>
        <div class="card-footer">
          <small>Rating: 4.0</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "search"
};
</script>

<style scoped>
</style>
