<template>
  <div class="container" style="padding-top:50px">
    <div class="row">
      <!-- user data display -->
      <div class="col-lg-6 col-md-12 col-sm-12 mx-auto">
        <div class="card">
          <div class="card-header my-info-header">My Info</div>
          <div class="card-body">
            <ul class="list-group">
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Name</div>
                  <div class="col-6">{{ userData.name }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Email</div>
                  <div class="col-6">{{ userData.email }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Major</div>
                  <div class="col-6">{{ userData.major }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Points</div>
                  <div class="col-6">{{ userData.points }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Liked Times</div>
                  <div class="col-6">{{ userData.likedNum }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Comment Times</div>
                  <div class="col-6">{{ userData.commentNum }}</div>
                </div>
              </li>
              <li class="list-group-item list-group-item-action">
                <div class="row">
                  <div class="col-6">Top up Number</div>
                  <div class="col-1"></div>
                  <div class="col-4">{{ userData.topNum }}</div>
                  <div class="col-1">
                    <i
                      class="fas fa-plus-circle float-right"
                      style="color:#f45905; margin-top:2px"
                      data-toggle="collapse"
                      data-target="#collapseExample"
                      aria-expanded="false"
                      aria-controls="collapseExample"
                    ></i>
                  </div>
                </div>
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
          this.$swal("Oops", err.response.data, "error");
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
.my-info-header {
  background-color: #6fc4b4;
  color: white;
}

.my-info-header:hover {
  background-color: #6bafa3;
}
</style>
