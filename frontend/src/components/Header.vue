<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <router-link class="navbar-brand" to="/">Peer Review</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar-collapse"
        aria-controls="navbar-collapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/" active-class="active" exact>Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/news" active-class="active" exact>News</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/search" active-class="active" exact>Search</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about" active-class="active" exact>About us</router-link>
          </li>
          <li class="nav-item" v-if="!$store.getters.isLoggedIn">
            <router-link class="nav-link" to="/login" active-class="active" exact>Log in</router-link>
          </li>
          <li class="nav-item dropdown" v-if="$store.getters.isLoggedIn">
            <a class="nav-link dropdown-toggle" data-toggle="dropdown">
              <i class="fas fa-user mr-2"></i>
              Hi, {{ this.$store.getters.getUserName }}
            </a>
            <div class="dropdown-menu dropdown-menu-right">
              <span class="dropdown-item" @click="goToMyAccount">My Account</span>
              <span class="dropdown-item" @click="goToMyProjects">My Projects</span>
              <div class="dropdown-divider"></div>
              <span class="dropdown-item" @click="logout">Log out</span>
            </div>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import $ from "jquery";

export default {
  name: "Header",
  methods: {
    logout() {
      if (this.$store.getters.isLoggedIn) {
        this.$swal({
          title: "Confirm",
          text: "Are you sure you want to log out?",
          type: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Log out"
        }).then(result => {
          if (result.value) {
            window.console.log("confirm result", result);
            this.$store.commit("logout");
            window.console.log("user logged out");
            if (this.$router.currentRoute.name !== "home") {
              this.$router.push({ name: "home" });
            }
            this.$swal("Success", "You are logged out!", "success").then(() => {
              window.location.reload(true);
            });
            // this.$axios
            //   .get("/api/users/logout/" + this.$store.getters.getUserId)
            //   .then(res => {
            //     if (res.status == 200) {
            //       this.$store.commit("logout");
            //       window.console.log("user logged out");
            //       if (this.$router.currentRoute.name !== "home") {
            //         this.$router.push({ name: "home" });
            //       }
            //       this.$swal("Success", "You are logged out!", "success").then(
            //         () => {
            //           window.location.reload(true);
            //         }
            //       );
            //     }
            //   })
            //   .catch(err => window.console.log(err));
          }
        });
      } else {
        window.console.log("User is already logged in!");
      }
    },
    goToMyAccount() {
      if (this.$router.currentRoute.name !== "myAccount") {
        this.$router.push({ name: "myAccount" });
      }
    },
    goToMyProjects() {
      if (this.$router.currentRoute.name !== "myProjects") {
        this.$router.push({ name: "myProjects" });
      }
    }
  },
  watch: {
    $route() {
      $("#navbar-collapse").collapse("hide");
    }
  }
};
</script>


<style scoped>
.navbar-light .navbar-brand {
  font-size: 2rem;
}

brand:focus,
.navbar-light .navbar-brand:hover {
  color: #9852f9;
}

.navbar {
  min-height: 100px;
}

.navbar-light .navbar-nav .nav-link.active {
  color: #9852f9;
}

.nav-item::after {
  content: "";
  display: block;
  width: 0px;
  height: 2px;
  background: #9852f9;
  transition: 0.2s;
}
.nav-item:hover::after {
  width: 100%;
}

.nav-link {
  padding: 15px 5px;
  transition: 0.2s;
}

.navbar-light .navbar-nav .nav-link.active {
  color: #9852f9;
}

.dropdown-menu {
  min-width: 0;
}
.dropdown-item {
  font-size: 14px;
  color: gray;
}

.dropdown-item:active {
  color: #212529;
}
.dropdown-item:focus,
.dropdown-item:hover {
  background: #9852f9;
}
</style> 