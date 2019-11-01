<template>
  <div class="container news-page">
      <h1>Your Major: {{$store.getters.getUserMajor}}</h1>
      <div>
          <p>News 1</p>
          <p>News 2</p>
      </div>
  </div>
</template>

<script>
export default {
  name: "news",
  components: {
  }
};
</script>

<style scoped>
.news-page {
  margin-top: 50px;
  margin-bottom: 100px;
}
</style>
