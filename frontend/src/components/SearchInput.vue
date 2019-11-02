<template>
  <div>
    <div class="search-input w-50 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
      <button class="my-btn form-control" @click="clickSearch">Search Project</button>
    </div>
    <span>Search Keyword: {{ searchData.keyword }} || Order Type: {{ searchData.orderType }}</span>
    <hr>
  </div>
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
  methods: {
    clickSearch() {
      window.console.log("search request in SearchInput");
      this.$emit("searchRequest");
    }
  }
};
</script>

<style scoped>
.search-input {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style> 