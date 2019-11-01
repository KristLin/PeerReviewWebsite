<template>
  <div class="container">
    <div class="row">
      <!-- file info display -->
      <div class="col-5">
        <div class="card" style="height: 400px;">
          <div class="card-header">{{ file.name }}</div>
          <div class="card-body">
            <pre><code class="text-left">{{ file.content }}</code></pre>
          </div>
          <div class="card-footer">
            <star-rating
              :inline="true"
              :read-only="true"
              :rating="file.mark"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="20"
            ></star-rating>
          </div>
        </div>
      </div>
      <!-- file info display end -->

      <!-- comments -->
      <div class="col-7">
        <div class="overflow-auto" style="height: 400px;">
          <div class="card mb-4">
            <div class="card-header">Comments</div>
            <div class="card-body" :key="idx" v-for="(comment, idx) in comments">
              <div class="row">
                <div class="col-4">
                  <p class="form-control">{{ comment.user }}</p>
                </div>
                <div class="col-8">
                  <p class="form-control">{{ comment.content }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- comments end -->
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "login",
  components: {
    StarRating
  },
  props: {},
  data() {
    return {
      file: this.$route.params.file,
      comments: [
        {
          id: "1",
          user: "krist",
          content: "Not bad",
          postTime: "2019-11-01 16:03:35"
        },
        {
          id: "2",
          user: "jack",
          content: "Good Job",
          postTime: "2019-11-02 12:19:20"
        }
      ]
    };
  },
  methods: {},
  created() {
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log(
        "lost params(file data), sending request to backend.."
      );
      this.file = {
        id: "6",
        name: "part2.txt",
        content:
          "He was working on a peer review website...\nAnd then he went crazy...",
        mark: 2.9
      };
    }
  }
};
</script>

<style scoped>
</style>
