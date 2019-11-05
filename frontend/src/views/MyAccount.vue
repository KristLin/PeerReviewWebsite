<template>
  <div class="container">
    <div class="row">
      <!-- user data display -->
      <div class="col-lg-6 col-md-6 col-sm-12">
        <div class="card">
          <div class="card-header">My Info</div>
          <div class="card-body">
            <p class="form-control border-0">Name: {{ userData.name }}</p>
            <p class="form-control border-0">Email: {{ userData.email }}</p>
            <p class="form-control border-0">Major: {{ userData.major }}</p>

            <p class="form-control border-0">Points: {{ userData.points }}</p>
            <p class="form-control border-0">Liked Number: {{ userData.likedNum }}</p>
            <p class="form-control border-0">Comment Number: {{ userData.commentNum }}</p>
            <p class="form-control border-0">Rest Top Number: {{ userData.topNum }}</p>
          </div>
          <div class="card-footer">
            <small>Registered Time: {{ userData.createdTime }}</small>
          </div>
        </div>
      </div>
      <!-- user data display end -->
    </div>
  </div>
</template>

<script>
export default {
  name: "myAccount",
  components: {},
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
  },
  created() {
    if (this.$store.getters.isLoggedIn) {
      this.$axios
        .get("/api/users/" + this.$store.getters.getUserId)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.userData = response.data;
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    } else {
      window.console.log("user is not logged in");
      this.$swal("Error", "Log in required!", "error");
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
</style>
