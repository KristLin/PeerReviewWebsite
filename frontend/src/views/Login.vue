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
              <button class="btn btn-primary form-control" @click="login">Log In</button>
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
          window.console.log("log in request")
      }
  }
};
</script>

<style scoped>
</style>
