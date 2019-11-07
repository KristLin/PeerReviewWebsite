<template>
  <div>
    <!-- carousel part -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div
          class="carousel-item"
          :class="{active: idx===0}"
          :key="idx"
          v-for="(item, idx) in carouselItems"
        >
          <img width="100%" height="100%" :src="item.imageSrc" />
          <div class="container">
            <div class="carousel-caption" :class="{'text-left': idx===0,'text-right':idx===2}">
              <h1>
                <strong>{{ item.title }}</strong>
              </h1>
              <h4>{{ item.description }}</h4>
              <button
                class="btn carousel-btn my-4"
                type="button"
                style="width:200px"
                @click="item.buttonClickFunction"
              >{{ item.buttonText }}</button>
            </div>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <!-- carousel part end -->

    <!-- features part -->
    <div class="features mx-auto">
      <div class="text-center">
        <h2 class="font-weight-bold my-4">Why choose us?</h2>
        <p class="lead mx-auto" style="margin-bottom: 70px">We provide a student only peer-review community.</p>
        <div class="row">
          <div class="col-lg-4 col-md-4 col-sm-12 px-2" :key="idx" v-for="(item, idx) in featureItems">
            <i class="fas feature-icon mb-4" :class="item.icon"></i>
            <h4 class="font-weight-bold mb-4">{{ item.title }}</h4>
            <p class="grey-text mb-md-0" style="margin-bottom: 2rem">{{ item.description}}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- features part end -->
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
      carouselItems: [
        {
          title: "Explore with us.",
          description: "Solve your problem in an easy way.",
          imageSrc: require("../../static/homepage-images/1.jpg"),
          buttonText: "Search",
          buttonClickFunction: () => {
            this.$router.push({
              name: "search"
            });
          }
        },
        {
          title: "Join us.",
          description: "Join us with thousands of users.",
          imageSrc: require("../../static/homepage-images/2.jpg"),
          buttonText: "Sign up here",
          buttonClickFunction: () => {
            this.$router.push({
              name: "signup"
            });
          }
        },
        {
          title: "Welcome.",
          description: "Try a better way to learn.",
          imageSrc: require("../../static/homepage-images/3.png"),
          buttonText: "Learn more",
          buttonClickFunction: () => {
            this.$router.push({
              name: "about"
            });
          }
        }
      ],
      featureItems: [
        {
          title: "Search Engine",
          description: "Find your interested projects in a easy way",
          icon: "fa-search"
        },
        {
          title: "Student Community",
          description: "Our users are students from all over the world.",
          icon: "fa-graduation-cap"
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
.carousel-item {
  height: 600px;
  background-color: black;
}
.carousel-item img {
  width: 100%;
  height: 600px;
  object-fit: cover;
  mask: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.6));
}

.carousel-btn {
  color: white;
  background-color: #6fc4b4;
}
.carousel-btn:hover {
  color: white;
  background-color: #6bafa3;
}

.features {
  width: 80%;
  margin-top: 5rem;
  margin-bottom: 3rem;
}

.feature-icon {
  font-size: 4rem;
}
@media screen and (max-width: 991px) {
  .carousel-caption h1 {
    font-size: 1.8rem;
  }

  .carousel-caption h4 {
    font-size: 1.4rem;
  }
  .carousel-item {
    height: 500px;
  }
  .carousel-item img {
    height: 500px;
  }
}

@media screen and (max-width: 767px) {
  .features {
    margin-bottom: 4rem;
  }
  .carousel-caption h1 {
    font-size: 1.4rem;
  }

  .carousel-caption h4 {
    font-size: 1rem;
  }
  .carousel-item {
    height: 450px;
  }
  .carousel-item img {
    height: 450px;
  }
}
</style>