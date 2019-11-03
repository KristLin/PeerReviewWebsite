<template>
  <div class="container">
    <div class="row">
      <!-- file info display -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px">
        <div class="card h-100 shadow">
          <div class="card-header my-bg font-weight-bold">{{ file.name }}</div>
          <div class="card-body overflow-auto">
            <highlight-code class="text-left" :lang="getLang(file.name)">{{ file.content }}</highlight-code>
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
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px">
        <Comments :comments="comments" />
      </div>
      <!-- comments end -->

      <div class="card mx-auto mt-4" style="width:550px">
        <div class="card-header p-2">
          <span class="text-muted mr-2">Your Mark:</span>
          <star-rating
            :inline="true"
            text-class="rating-text"
            v-bind:increment="1"
            v-bind:star-size="20"
            v-model="commentData.mark"
          ></star-rating>
        </div>
        <div class="card-body">
          <textarea
            class="form-control mb-2"
            v-model="commentData.content"
            cols="30"
            rows="5"
          ></textarea>
          <button class="my-btn form-control" @click="leaveReview">Leave a review</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import Comments from "@/components/Comments.vue";

export default {
  name: "file",
  components: {
    StarRating,
    Comments
  },
  props: {},
  data() {
    return {
      file: this.$route.params.file,
      comments: [
        {
          id: "1",
          user: "krist",
          content:
            "Not bad Not bad Not bad Not bad Not bad Not bad Not bad Not bad Not bad Not bad Not bad",
          postTime: "2019-11-01 16:03:35",
          likedNum: 3,
          hasLiked: true
        },
        {
          id: "2",
          user: "jack",
          content: "Good Job",
          postTime: "2019-11-02 12:19:20",
          likedNum: 50,
          hasLiked: false
        },
        {
          id: "3",
          user: "krist",
          content: "Ahhhhhhhhhh",
          postTime: "2019-11-01 15:05:35",
          likedNum: 11,
          hasLiked: true
        },
        {
          id: "4",
          user: "jack",
          content: "Just a test test test test test",
          postTime: "2019-11-02 11:00:30",
          likedNum: 23,
          hasLiked: true
        },
        {
          id: "5",
          user: "krist",
          content: "I don't like it",
          postTime: "2019-11-02 18:03:35",
          likedNum: 0,
          hasLiked: false
        },
        {
          id: "6",
          user: "jack",
          content: "Looks good tho",
          postTime: "2019-10-30 12:01:00",
          likedNum: 1,
          hasLiked: false
        }
      ],
      commentData: {
        mark: 0,
        content: ""
      }
    };
  },
  methods: {
    getLang(fileName) {
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
    },
    leaveReview() {
      this.$swal({
        title: "Success",
        text:
          "Mark: " +
          this.commentData.mark +
          "Content: " +
          this.commentData.content,
        type: "success"
      });
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
</style>
