<template>
  <div class="container">
    <div class="row">
      <!-- user data display -->
      <div class="col-lg-6 col-md-6 col-sm-12">
        <div class="card">
          <div class="card-header">
            My Info
          </div>
          <div class="card-body">
            <p class="form-control border-0">Name: {{ userData.name }}</p>
            <p class="form-control border-0">Email: {{ userData.email }}</p>
            <p class="form-control border-0">Major: {{ userData.major }}</p>

            <p class="form-control border-0">Points: {{ userData.points }}</p>
            <p class="form-control border-0">Liked Times: {{ userData.likedTimes }}</p>
            <p class="form-control border-0">Comment Times: {{ userData.commentTimes }}</p>
            <p class="form-control border-0">Rest Top Times: {{ userData.topTimes }}</p>
          </div>
          <div class="card-footer">
            <small>Registered Time: {{ userData.registeredTime }}</small>
          </div>
        </div>
      </div>
      <!-- user data display end -->

      <!-- rank -->
      <div class="col-lg-6 col-md-6 col-sm-12">
        <Rank />
      </div>
      <!-- rank end -->
    </div>
  </div>
</template>

<script>
import Rank from "@/components/Rank.vue"

export default {
  name: "myAccount",
  components: {
    Rank
  },
  data() {
    return {
      userData: {
        id: "1",
        name: "Krist",
        email: "krist@mail.com",
        major: "CSE",
        points: 1020,
        likedTimes: 56,
        commentTimes: 22,
        topTimes: 9,
        registeredTime: new Date().toLocaleString("en-GB")
      }
    };
  }
};
</script>

<style scoped>
</style>
