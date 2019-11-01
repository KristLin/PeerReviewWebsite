<template>
  <div class="project-list overflow-auto" style="height: 500px;">
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Project Title</h5>
        <p>Project Description</p>
      </div>
      <div class="card-footer">
        <star-rating
          :inline="true"
          :read-only="true"
          :rating="4"
          :show-rating="false"
          v-bind:increment="0.01"
          v-bind:star-size="20"
        ></star-rating>
      </div>
    </div>
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Project Title</h5>
        <p>Project Description</p>
      </div>
      <div class="card-footer">
        <star-rating
          :inline="true"
          :read-only="true"
          :rating="4"
          :show-rating="false"
          v-bind:increment="0.01"
          v-bind:star-size="20"
        ></star-rating>
      </div>
    </div>
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Project Title</h5>
        <p>Project Description</p>
      </div>
      <div class="card-footer">
        <star-rating
          :inline="true"
          :read-only="true"
          :rating="4"
          :show-rating="false"
          v-bind:increment="0.01"
          v-bind:star-size="20"
        ></star-rating>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "ProjectList",
  components: {
    StarRating
  }
};
</script>

<style scoped>
</style> 