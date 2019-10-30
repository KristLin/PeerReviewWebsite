<template>
  <div class="search-input w-50 mx-auto">
    <input type="text" class="form-control" placeholder="Keyword" />
    <button class="my-btn form-control">Search Project</button>
  </div>
</template>

<script>
export default {
  name: "SearchInput"
};
</script>

<style scoped>
.search-input {
  margin-top: 50px;
  margin-bottom: 50px;
}

.my-btn {
  border: none;
  background-color: #c299fc;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #9852f9;
  color: white;
}
</style> 