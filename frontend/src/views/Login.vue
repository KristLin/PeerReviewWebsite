<template>
  <div class="container">
    <div class="card mx-auto shadow login-form">
      <i class="fas fa-user-circle fa-6x card-img-top mx-auto mt-4"></i>
      <div class="card-body">
        <h5 class="card-title">Login</h5>
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            v-model="loginData.email"
            placeholder="Email Address"
          />
        </div>
        <div class="form-group">
          <input
            type="password"
            class="form-control"
            v-model="loginData.password"
            placeholder="Password"
          />
        </div>
        <div class="form-group">
          <button class="my-btn form-control" @click="login">Log In</button>
        </div>
      </div>
      <div class="card-footer">
        <small class="mb-4">
          Not a member yet?
          <router-link class="mx-1" to="/signup">Sign up</router-link>here!
        </small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      loginData: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      // raise alert if login form is not complete
      for (let key in this.loginData) {
        if (this.loginData[key] === "") {
          this.$swal("Warning", "The login form is not complete!", "warning");
          return;
        }
      }

      this.$axios
        .post("/api/users/login", this.loginData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            let [userId, userMajor, userName] = response.data.split(" ");
            let authUserData = {
              userId: userId,
              userMajor: userMajor,
              userName: userName
            };
            this.$store.commit("login", authUserData);
            this.$swal({
              title: "Success",
              text: "You are logged in!",
              type: "success"
            });
            this.$router.push({
              name: "myProjects"
            });
          }
        })
        .catch(err => {
          this.$swal("Oops", err.response.data, "error");
          window.console.log(err.response.data);
        });
    }
  }
};
</script>

<style scoped>
.login-form {
  width: 350px;
}
</style>
