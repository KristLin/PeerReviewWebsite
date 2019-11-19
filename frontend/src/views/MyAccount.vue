<template>
  <div class="container" style="padding-top:50px">
    <!-- user data display -->
    <div class="my-info mx-auto">
      <div class="card">
        <div class="card-header my-info-header">My Information</div>
        <div class="card-body">
          <ul class="list-group">
            <!-- user name -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Name</div>
                <div class="col-7">{{ userData.name }}</div>
              </div>
            </li>

            <!-- user email -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Email</div>
                <div class="col-7">{{ userData.email }}</div>
              </div>
            </li>

            <!-- user major -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Major</div>
                <div class="col-7">{{ userData.major }}</div>
              </div>
            </li>

            <!-- user points -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Points</div>
                <div class="col-7">{{ userData.points }}</div>
              </div>
            </li>

            <!-- user liked number -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Liked Times</div>
                <div class="col-7">{{ userData.likedNum }}</div>
              </div>
            </li>

            <!-- user comment number -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Comment Times</div>
                <div class="col-7">{{ userData.commentNum }}</div>
              </div>
            </li>

            <!-- user top up number -->
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-5">Top up Number</div>
                <div class="col-2"></div>
                <div class="col-3">{{ userData.topNum }}</div>
                <!-- exchange top up button start -->
                <div class="col-2">
                  <i
                    class="fas fa-plus-circle float-right"
                    style="color:#f45905; margin-top:3px"
                    data-toggle="collapse"
                    data-target="#collapseExample"
                    aria-expanded="false"
                    aria-controls="collapseExample"
                  ></i>
                </div>
                <!-- exchange top up button end -->
              </div>
            </li>

            <!-- delete account button -->
            <button class="form-control w-50 btn btn-danger mx-auto mt-4" @click="deleteAccount">
              <i class="fas fa-trash-alt mr-2" style="color:white"></i>Delete Account
            </button>
          </ul>
        </div>
        <!-- user registered time -->
        <div class="card-footer">
          <small>Registered Time: {{ userData.createdTime }}</small>
        </div>
      </div>

      <!-- exchange points to top up number -->
      <!-- collapse controlled by the "plus" button in top up number row -->
      <div class="collapse mx-auto" id="collapseExample" style="width:80%">
        <input
          type="text"
          class="form-control mt-4 mb-2"
          placeholder="10 Points = 1 Top up"
          v-model="exchangeTopNumStr"
        />
        <button class="form-control btn btn-warning" @click="exchangeTopUp">Exchange Top Ups</button>
      </div>
    </div>
    <!-- user data display end -->
  </div>
</template>

<script>
export default {
  name: "myAccount",
  components: {},
  data() {
    return {
      userData: {},
      exchangeTopNumStr: ""
    };
  },
  methods: {
    // user exchange top up number using points
    exchangeTopUp() {
      window.console.log("exchange top num request");
      if (this.exchangeTopNumStr === "") {
        this.$swal("Warning", "Please input the number of Top Ups", "warning");
        return;
      }
      // parse the string input to an integer
      var exchangeTopNum = parseInt(this.exchangeTopNumStr);
      // reset the input
      this.exchangeTopNumStr = "";
      // send request to backend
      this.$axios
        .get("/api/users/exchange_topup", {
          params: {
            exchangeTopNum: exchangeTopNum,
            user_id: this.$store.getters.getUserId
          }
        })
        .then(response => {
          // update the top up number and points locally in frontend
          if (response.status == 200) {
            this.userData.points -= exchangeTopNum * 10;
            this.userData.topNum += exchangeTopNum;
          }
        })
        .catch(err => {
          this.$swal("Oops", err.response.data, "error");
        });
    },
    // delete user account
    deleteAccount() {
      // show a dialog to confirm user's request
      this.$swal({
        title: "Confirm",
        text: "Are you sure to delete account?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Delete"
      }).then(result => {
        if (result.value) {
          // send delete request to backend
          this.$axios
            .delete("/api/users/" + this.$store.getters.getUserId)
            .then(res => {
              if (res.status == 200) {
                this.$store.commit("logout");
                window.console.log("user account is deleted");
                this.$swal("Success", "Your account is deleted!", "success");
                // take user back to home page
                this.$router.push({ name: "home" });
                window.location.reload(true);
              }
            })
            .catch(err => window.console.log(err));
        }
      });
    }
  },
  created() {
    // used for debugging
    window.console.log(
      this.$store.getters.getUserId,
      this.$store.getters.getUserName
    );

    // check if user has logged in
    if (this.$store.getters.isLoggedIn) {
      // get user data from backend
      this.$axios
        .get("/api/users/" + this.$store.getters.getUserId)
        .then(response => {
          if (response.status == 200) {
            this.userData = response.data;
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    // take user to login page if not logged in yet
    } else {
      window.console.log("user is not logged in");
      this.$swal("Error", "Log in required!", "error");
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
.my-info {
  width: 500px;
}

@media screen and (max-width: 625px) {
  .my-info {
    width: 100%;
  }
}

.my-info-header {
  background-color: #6fc4b4;
  color: white;
}

.my-info-header:hover {
  background-color: #6bafa3;
}
</style>
