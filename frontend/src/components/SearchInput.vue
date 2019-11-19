<template>
  <div class="w-50 mx-auto">
    <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
  </div>
</template>

<script>
export default {
  name: "SearchInput",
  props: {
    searchData: {
      keyword: "",
    }
  },
};
</script>

<style scoped>
</style> 