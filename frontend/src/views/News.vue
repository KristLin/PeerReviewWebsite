<template>
  <div class="container news-page" style="padding-top:50px">
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
  components: {}
};
</script>

<style scoped>
.news-page {
  min-height: 500px;
}
</style>
