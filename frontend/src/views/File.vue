<template>
  <div class="container">
    <div class="row">
      <!-- file info display -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:500px">
        <div class="card h-100">
          <div class="card-header my-bg font-weight-bold">{{ file.name }}</div>
          <div class="card-body overflow-auto">
            <highlight-code class="text-left" :lang="getFileLang(file.name)">{{ file.content }}</highlight-code>
          </div>
          <div class="card-footer">
            <star-rating
              :inline="true"
              :read-only="true"
              :rating="file.mark"
              :show-rating="true"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="file.mark>0"
            ></star-rating>
            <small v-if="file.mark===0">This file hasn't received any mark yet...</small>
          </div>
        </div>
      </div>
      <!-- file info display end -->

      <!-- comments -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:500px">
        <div class="overflow-auto h-100">
          <div class="card mb-4" :key="idx" v-for="(comment, idx) in comments">
            <div class="card-body">
              <div class="row">
                <div class="col-4">
                  <p>{{ comment.user }}</p>
                </div>
                <div class="col-8">
                  <p>{{ comment.content }}</p>
                </div>
              </div>
            </div>
            <div class="card-footer p-1">
              <small>{{ comment.postTime }}</small>
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
  methods: {
    getFileLang(fileName) {
      let fileLang = fileName.split(".").pop();
      switch (fileLang) {
        case "py":
          return "python";
        case "js":
          return "javascript";
        case "java":
          return "java";
        case "txt":
          return "plaintext";
        case "html":
          return "html";
        case "css":
          return "css";
        case "php":
          return "php";
        default:
          return "plaintext";
      }
    }
  },
  created() {
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log(
        "lost params(file data), sending request to backend.."
      );
      this.file = {
        id: "1",
        name: "index.html",
        content: "<h1>Hello World</h1>\n<h1>Bye World</h1>",
        mark: 3.8
      };
    }
  }
};
</script>

<style scoped>
.hljs {
  height: 100%;
  display: table;
}
</style>
