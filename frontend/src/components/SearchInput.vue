<template>
  <div class="w-50 mx-auto">
    <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
  </div>
  <!-- <span>Search Keyword: {{ searchData.keyword }} || Order Type: {{ searchData.orderType }}</span> -->
</template>

<script>
export default {
  name: "SearchInput",
  props: {
    searchData: {
      keyword: "",
      orderType: ""
    }
  },
  methods: {}
};
</script>

<style scoped>
</style> 