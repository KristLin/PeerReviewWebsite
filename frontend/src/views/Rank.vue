<template>
  <div class="container" style="padding-top:50px">
    <!-- <div class="row cloud-div">
      <img src="../../static/cloud.png" class="cloud-image-top" />
      <img src="../../static/cloud.png" class="cloud-image-mid" />
      <img src="../../static/cloud.png" class="cloud-image-bottom" />
    </div> -->

    <!-- Loading -->
    <div v-if="!hasFetchedData" style="margin-top: 120px; margin-bottom:200px">
      <h4 class="my-4">Loading ...</h4>
      <b-spinner variant="secondary" style="width: 5rem; height: 5rem; font-size:2rem;" label="Loading..."></b-spinner>
    </div>

    <ul class="list-group mx-auto border rank-list" v-if="hasFetchedData">
      <li class="list-group-item active my-bg">
        <h4 class="my-4">User Points Ranking</h4>
        <div class="row">
          <p class="col-4 m-0">Name</p>
          <p class="col-4 m-0">Major</p>
          <p class="col-4 m-0">Points</p>
        </div>
      </li>
      
      <!-- only display top 5 -->
      <li class="list-group-item list-group-item-action" :key="idx" v-for="(user, idx) in top10.slice(0,5)">
        <div class="row rank-user-row">
          <div class="col-4">{{ user.name }}</div>
          <div class="col-4">
            <i class="fas fa-laptop-code user-major-icon" v-if="user.major === 'CSE'"></i>
            <i class="fas fa-user-tie user-major-icon" v-if="user.major === 'Business'"></i>
            <i class="fas fa-stethoscope user-major-icon" v-if="user.major === 'Medical'"></i>
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
      top10: [],
      hasFetchedData: false,
    };
  },
  created() {
    this.$axios
      .get("/api/users/top10")
      .then(response => {
        if (response.status == 200) {
          this.top10 = response.data;
          this.hasFetchedData = true;
        }
      })
      .catch(err => {
        window.console.log(err.response);
      });
  }
};
</script>

<style scoped>
.rank-list {
  min-height:400px;
  width: 500px;
}

.rank-user-row {
  line-height: 2.5rem;
}

@media screen and (max-width: 625px) {
  .rank-list {
    width: 100%;
  }
}

.user-major-icon {
  color: #6bafa3;
  font-size: 1.3rem;
}
</style>
