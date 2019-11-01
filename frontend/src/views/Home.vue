<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div>
      image + learnmore button
    </div>
    <hr>
    <!-- 2. more on homepage -->
    <div class="features mx-auto">
      <div class="text-center">
        <h2 class="font-weight-bold my-4">Why is it so great?</h2>
        <p class="lead mx-auto" style="margin-bottom: 70px">We offer you best user experience.</p>
        <div class="row">
          <div class="col-lg-4 col-md-4 col-sm-12" :key="idx" v-for="(item, idx) in featureItems">
            <i class="fas feature-icon mb-4" :class="item.icon"></i>
            <h4 class="font-weight-bold mb-4">{{ item.title }}</h4>
            <p class="grey-text mb-md-0" style="margin-bottom: 2rem">{{ item.description}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "home",
  components: {
    // SearchInput,
    // HouseCards
  },
  props: {},
  data() {
    return {
      
      featureItems: [
        {
          title: "Search Engine",
          description: "Search the houses in the way you like, even in map.",
          icon: "fa-search"
        },
        {
          title: "Save Money",
          description: "We offer price worthy renting houses.",
          icon: "fa-money-bill-alt"
        },
        {
          title: "Reviews & Ratings",
          description: "Share your review and rating with others.",
          icon: "fa-comments"
        }
      ]
    };
  },

  methods: {}
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}

.features {
  width: 80%;
  margin-top: 5rem;
  margin-bottom: 8rem;
}

.feature-icon {
  font-size: 4rem;
}

@media screen and (max-width: 780px) {
  .feature-icon {
    font-size: 3rem;
  }
}

@media screen and (max-width: 767px) {
  .features {
    margin-bottom: 4rem;
  }
}
</style>