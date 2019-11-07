<template>
  <div class="container" style="padding-top:50px">
    <div class="card mx-auto shadow singup-form">
      <i class="fas fa-user-circle fa-6x card-img-top mx-auto mt-4"></i>
      <div class="card-body">
        <h5 class="card-title">Singup</h5>

        <div class="form-group">
          <input
            type="email"
            class="form-control"
            v-model="userData.email"
            placeholder="Email Address"
          />
        </div>

        <div class="form-group">
          <input type="text" class="form-control" v-model="userData.name" placeholder="Your Name" />
        </div>

        <div class="form-group">
          <select v-model="userData.major" class="form-control">
            <option value="Your Major">Your Major</option>
            <option value="CSE">Computer Science & Engineering</option>
            <option value="Business">Business</option>
            <option value="Medical">Medical</option>
            <option value="Literature">Literature</option>
          </select>
        </div>

        <div class="form-group">
          <input
            type="password"
            class="form-control"
            v-model="userData.password"
            placeholder="Password"
          />
        </div>

        <div class="form-group">
          <input
            type="password"
            class="form-control"
            v-model="checkedData.password2"
            placeholder="Password Confirm"
          />
        </div>

        <div class="form-group">
          <button class="my-btn form-control" @click="signup">Sign up</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "singup",
  data() {
    return {
      userData: {
        name: "",
        email: "",
        password: "",
        major: "Your Major"
      },
      checkedData: {
        password2: ""
      }
    };
  },
  methods: {
    signup() {
      // raise alert if user info is not complete
      for (let key in this.userData) {
        if (this.userData[key] === "") {
          this.$swal(
            "Warning",
            "The register form is not complete (" + key + ")!",
            "warning"
          );
          return;
        }
      }

      if (this.userData.major === "Your Major") {
        this.$swal("Warning", "You didn't choose a major!", "warning");
        return;
      }

      // raise alert if two password are not matched
      if (this.userData.password !== this.checkedData.password2) {
        this.$swal("Warning", "Two passwords are not matched", "warning");
        return;
      }

      // raise alert if email is not a valid @edu email
      if (this.userData.email.includes("@")) {
        if (!this.userData.email.split("@")[1].includes("edu")) {
          this.$swal("Warning", "Email is not a student email.", "warning");
          return;
        }
      } else {
        this.$swal("Warning", "Invliad email format.", "warning");
        return;
      }

      this.$axios
        .post("/api/users/", this.userData)
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
              text: "You are registered!",
              type: "success"
            });
            this.$router.push({
              name: "myProjects"
            });
          }
        })
        .catch(err => {
          this.$swal("Oops", err.response.data, "error");
          window.console.log(err.response);
        });
    }
  }
};
</script>

<style scoped>
.singup-form {
  width: 350px;
}

@media screen and (max-width: 450px) {
  .singup-form {
    width: 100%;
  }
}
</style>
