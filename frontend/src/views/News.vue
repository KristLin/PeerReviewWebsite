<template>
  <div class="container" style="padding-top:50px">
    <div v-if="!this.$store.getters.isLoggedIn">
      <i class="fas fa-question major-icon"></i>
      <!-- <h3 class="mt-4 mb-2">You are not logged in</h3> -->
      <p class="my-4">
        News subject is randomly picked.
        <router-link class="mx-1" to="/login">Log in</router-link>to see news in your major!
      </p>
    </div>
    <!-- major icon -->
    <div v-if="this.$store.getters.isLoggedIn">
      <i class="fas fa-laptop-code major-icon" v-if="$store.getters.getUserMajor === 'CSE'"></i>
      <i class="fas fa-user-tie major-icon" v-if="$store.getters.getUserMajor === 'Business'"></i>
      <i class="fas fa-stethoscope major-icon" v-if="$store.getters.getUserMajor === 'Medical'"></i>
      <i class="fas fa-book major-icon" v-if="$store.getters.getUserMajor === 'Literature'"></i>
    </div>

    <!-- Loading -->
    <div v-if="!hasFetchedData" style="margin-top: 80px; margin-bottom:100px">
      <h4 class="my-4">Loading ...</h4>
      <b-spinner variant="secondary" style="width: 5rem; height: 5rem; font-size:2rem;"  label="Loading..."></b-spinner>
    </div>
    

    <div v-if="hasFetchedData" style="margin-top: 50px">
      <h4 class="mt-4 mb-0 text-muted my-4"></h4>
      <ul class="list-group mx-auto news-list">
        <li class="list-group-item active my-bg">
          <h4>News</h4>
          <small style="color:white">Click an article to see more</small>
        </li>
        <li
          class="list-group-item list-group-item-action"
          :key="idx"
          v-for="(news_item, idx) in news"
        >
          <a :href="news_item.href">{{ news_item.heading }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "news",
  data() {
    return {
      news: [],
      hasFetchedData: false
    };
  },
  components: {},
  created() {
    var major = "";
    if (this.$store.getters.isLoggedIn) {
      major = this.$store.getters.getUserMajor;
    }
    this.$axios
      .get("/api/news", { params: { major: major } })
      .then(res => {
        this.news = res.data;
        this.hasFetchedData = true;
      })
      .catch(err => {
        window.console.log(err.response.data);
      });
  }
};
</script>

<style scoped>
.news-list {
  width: 600px;
}

@media screen and (max-width: 650px) {
  .news-list {
    width: 100%;
  }
}

.news-list a {
  color: #366b60;
}

.major-icon {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  color: #6fc4b4;
  line-height: 100px;
  text-align: center;
  background: rgba(180, 175, 175, 0.25);
  font-weight: bold;
  font-size: 2.5rem;
}

.major-icon:hover {
  color: #6bafa3;
}
</style>
