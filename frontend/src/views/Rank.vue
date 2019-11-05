<template>
  <div class="container">
    <ul class="list-group mx-auto border" style="width:350px;min-height:500px">
      <li class="list-group-item active my-bg">
        <p>User Points Ranking</p>
        <div class="row">
          <small class="col-4">Name</small>
          <small class="col-4">Major</small>
          <small class="col-4">Points</small>
        </div>
      </li>
      <li class="list-group-item list-group-item-action" :key="idx" v-for="(user, idx) in top10">
        <div class="row">
          <div class="col-4">{{ user.name }}</div>
          <div class="col-4">
            <i class="fas fa-laptop-code user-major-icon" v-if="user.major === 'CSE'"></i>
            <i class="fas fa-user-tie user-major-icon" v-if="user.major === 'Business'"></i>
            <i class="fas fa-user-md user-major-icon" v-if="user.major === 'Medical'"></i>
            <i class="fas fa-book user-major-icon" v-if="user.major === 'Literature'"></i>
          </div>
          <div class="col-4">{{ user.points }}</div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "rank",
  data() {
    return {
      top10: []
    };
  },
  created() {
    this.$axios
      .get("/api/users/top10")
      .then(response => {
        if (response.status == 200) {
          this.top10 = response.data;
        }
      })
      .catch(err => {
        window.console.log(err.response);
      });
  }
};
</script>

<style scoped>
.my-bg.list-group-item.active {
  border: none;
  background-color: #7ecfc0;
  color: white;
}

.my-bg:hover.list-group-item.active {
  border: none;
  background-color: #6bafa3;
  color: white;
}

.user-major-icon {
  color: #6bafa3;
  font-size: 1rem;
}
</style>
