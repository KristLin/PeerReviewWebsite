<template>
  <div id="app">
    <Header />
    <div class="content-div">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Header,
    Footer
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Nunito&display=swap");
#app {
  font-family: "Nunito", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.content-div {
  margin-top: 150px;
  margin-bottom: 100px;
}

.form-control.my-btn {
  border: none;
  background-color: #c299fc;
  color: white;
}

.form-control.my-btn:hover {
  border: none;
  background-color: #9852f9;
  color: white;
}

.my-bg {
  background-color: #c299fc !important;
  color: white;
}

.my-hr {
  border: dotted #9852f9 5px;
  border-bottom: none;
  width: 20%;
}
</style>
