<template>
  <div>
    <div class="login-form">
      <div class="card shadow mx-auto" style="width: 300px;">
        <i class="fas fa-user-circle fa-6x card-img-top mx-auto mt-4"></i>
        <div class="card-body">
          <h5 class="card-title">Login</h5>
            <div class="form-group">
              <input type="text" class="form-control" name="username" placeholder="Username" />
            </div>
            <div class="form-group">
              <input type="password" class="form-control" name="password" placeholder="Password" />
            </div>
            <div class="form-group">
              <button class="my-btn form-control" @click="login">Log In</button>
            </div>
        </div>
        <div class="card-footer">
          <small class="mb-4">Don't have an account yet? Sign up here!</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
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
              userRole: userMajor,
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
