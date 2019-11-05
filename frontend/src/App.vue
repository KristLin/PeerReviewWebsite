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
  padding-top: 150px;
  padding-bottom: 100px;
}

.form-control.my-btn {
  border: none;
  background-color: #7ecfc0;
  color: white;
}

.form-control.my-btn:hover {
  border: none;
  background-color: #6bafa3;
  color: white;
}

.my-bg.card-header {
  background-color: #7ecfc0;
  color: white;
}

.card:hover .my-bg.card-header {
  background-color: #6bafa3;
  color: white;
}

.zoom:hover {
  transform: scale(1.3);
}
</style>
