<template>
  <div class="container login-form">
    <div class="card shadow">
      <i class="fas fa-user-circle fa-6x card-img-top mx-auto mt-4"></i>
      <div class="card-body">
        <h5 class="card-title">Login</h5>
        <div class="form-group">
          <input type="text" class="form-control" v-model="loginData.email" placeholder="Email Address" />
        </div>
        <div class="form-group">
          <input type="password" class="form-control" v-model="loginData.password" placeholder="Password" />
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
    }
  },
  methods: {
    login() {
      // raise alert if login form is not complete
      for (let key in this.loginData) {
        if (this.loginData[key] === "") {
          alert("The login form is not complete!");
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
            alert("logged in!");
            this.$router.push({
              name: "home"
            });
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  }
};
</script>

<style scoped>
.login-form {
  width: 300px;
  margin-top: 50px;
  margin-bottom: 100px;
}

.my-btn {
  border: none;
  background-color: #c299fc;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #9852f9;
  color: white;
}
</style>
