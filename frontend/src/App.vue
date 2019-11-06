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
@import url('https://fonts.googleapis.com/css?family=Varela+Round&display=swap');
#app {
  font-family: 'Varela Round', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.content-div {
  padding-top: 100px;
  padding-bottom: 100px;
}

.form-control.my-btn {
  border: none;
  background-color: #6fc4b4;
  color: white;
}

.form-control.my-btn:hover {
  border: none;
  background-color: #6bafa3;
  color: white;
}

.my-bg.card-header {
  background-color: #6fc4b4;
  color: white;
}

.card:hover .my-bg.card-header {
  background-color: #6bafa3;
  color: white;
}

.my-bg.list-group-item.active {
  border: none;
  background-color: #6fc4b4;
  color: white;
}

.my-bg:hover.list-group-item.active {
  border: none;
  background-color: #6bafa3;
  color: white;
}

.zoom:hover {
  transform: scale(1.3);
}

.swal2-popup {
  font-size: 0.7rem !important;
}
</style>
