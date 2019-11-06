<template>
  <div class="container" style="padding-top:50px">
    <div class="row">
      <!-- user data display -->
      <div class="my-info mx-auto">
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
                  <div class="col-2"></div>
                  <div class="col-2">{{ userData.topNum }}</div>
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
                </div>
              </li>
              <button class="form-control w-50 btn btn-danger mx-auto mt-4" @click="deleteAccount">
                <i class="fas fa-trash-alt mr-2" style="color:white"></i>Delete Account
              </button>
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
      userData: {},
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
    },
    deleteAccount() {
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
          this.$axios
            .delete("/api/users/" + this.$store.getters.getUserId)
            .then(res => {
              if (res.status == 200) {
                this.$store.commit("logout");
                window.console.log("user account is deleted");
                this.$swal("Success", "Your account is deleted!", "success");
                this.$router.push({ name: "home" });
              }
            })
            .catch(err => window.console.log(err));
        }
      });
    }
  },
  created() {
    window.console.log(this.$store.getters.getUserId, this.$store.getters.getUserName)
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
.my-info {
  width: 500px;
}

@media screen and (max-width: 550px) {
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
