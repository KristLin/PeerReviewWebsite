<template>
  <div class="project-info overflow-auto" style="height: 500px;">
    <div class="card mb-4">
      <div class="card-header">Project Title</div>
      <div class="card-body">
        <p>Project Description</p>
      </div>
      <div class="card mx-4 my-4">
        <div class="card-header">File List:</div>
        <div class="card-body text-left">
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
          <p class="file-name" @click="$router.push({name: 'file'})">file1.txt</p>
        </div>
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
.file-name:hover {
  color: #9852f9;
}
</style> 