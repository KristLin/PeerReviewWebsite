<template>
  <div class="container">
    <div class="row">
      <!-- user data display -->
      <div class="col-lg-6 col-md-12 col-sm-12 mx-auto">
        <div class="card">
          <div class="card-header">My Info</div>
          <div class="card-body">
            <ul class="list-group">
              <li class="list-group-item list-group-item-action">Name: {{ userData.name }}</li>
              <li class="list-group-item list-group-item-action">Email: {{ userData.email }}</li>
              <li class="list-group-item list-group-item-action">Major: {{ userData.major }}</li>
              <li class="list-group-item list-group-item-action">Points: {{ userData.points }}</li>
              <li
                class="list-group-item list-group-item-action"
              >Liked Number: {{ userData.likedNum }}</li>
              <li
                class="list-group-item list-group-item-action"
              >Comment Number: {{ userData.commentNum }}</li>
              <li class="list-group-item list-group-item-action">
                Rest Top up Number: {{ userData.topNum }}
                <i
                  class="fas fa-plus-circle float-right mt-1"
                  type="button"
                  style="color:#f45905"
                  data-toggle="collapse"
                  data-target="#collapseExample"
                  aria-expanded="false"
                  aria-controls="collapseExample"
                ></i>
              </li>
            </ul>
          </div>
          <div class="card-footer">
            <small>Registered Time: {{ userData.createdTime }}</small>
          </div>
        </div>

        <div class="collapse mx-auto" id="collapseExample" style="width:80%">
          <input
            type="text"
            class="form-control mt-4 mb-2"
            placeholder="Number of Top Ups"
            v-model="buyTopNumStr"
          />
          <button class="form-control btn btn-warning" @click="buyTopUp">Buy Top Ups</button>
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
        likedNum: 56,
        commentNum: 22,
        topNum: 9,
        registeredTime: new Date().toLocaleString("en-GB")
      },
      buyTopNumStr: ""
    };
  },
  methods: {
    buyTopUp() {
      window.console.log("buy top num request");
      if (this.buyTopNumStr === "") {
        this.$swal("Warning", "Please input the number of Top Ups", "warning");
        return;
      }
      var buyTopNum = parseInt(this.buyTopNumStr);
      this.buyTopNumStr = "";
      this.$axios
        .get("/api/users/buy_topup", {
          params: {
            buyTopNum: buyTopNum,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          if (response.status == 200) {
            this.userData.points -= buyTopNum * 10;
            this.userData.topNum += buyTopNum;
          }
        })
        .catch(err => {
          this.$swal("Error", err.response.data, "error");
        });
    }
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
