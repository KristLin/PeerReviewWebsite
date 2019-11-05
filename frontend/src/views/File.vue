<template>
  <div class="container">
    <div class="row">
      <!-- file info display -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px">
        <div class="card h-100 shadow" v-if="!file"></div>
        <div class="card h-100 shadow" v-if="file">
          <div class="card-header my-bg font-weight-bold">{{ file.name }}</div>
          <div class="card-body overflow-auto">
            <highlight-code class="text-left" :lang="getLang(file.name)">{{ file.content }}</highlight-code>
          </div>
          <div class="card-footer">
            <star-rating
              :inline="true"
              :read-only="true"
              :rating="file.rating"
              :show-rating="true"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="file.rating>0"
            ></star-rating>
            <small v-if="file.rating===0">This file hasn't received any rating yet...</small>
          </div>
        </div>
      </div>
      <!-- file info display end -->

      <!-- comments -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px">
        <Comments :comments="comments" @likeComment="likeComment" />
      </div>
      <!-- comments end -->

      <!-- leave review -->
      <div class="card mx-auto shadow-sm mt-4" style="width:550px">
        <div class="card-header p-2">
          <span class="text-muted mr-2">Your Rating:</span>
          <star-rating
            :inline="true"
            text-class="rating-text"
            v-bind:increment="1"
            v-bind:star-size="20"
            v-model="commentData.rating"
          ></star-rating>
        </div>
        <div class="card-body">
          <textarea class="form-control mb-2" v-model="commentData.content" cols="30" rows="5"></textarea>
          <button class="my-btn form-control" @click="leaveReview">Leave a review</button>
        </div>
      </div>
      <!-- leave review end -->
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
      comments: [],
      commentData: {
        rating: 5,
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
      if (!this.$store.getters.isLoggedIn) {
        this.$swal("Warning", "Log in required!", "warning");
        this.$router.push({ name: "login" });
        return;
      }
      if (this.commentData.content === "") {
        this.$$swal("Warnning", "You didn't input any content!", "warning");
        return;
      }

      this.commentData.user = this.$store.getters.getUserId;
      this.commentData.userName = this.$store.getters.getUserName;
      this.commentData.file = this.file._id;

      this.$axios
        .post("/api/comments/", this.commentData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            // this.commentData.createdTime = new Date().toLocaleString("en-GB");
            // this.commentData.hasLiked = false;
            // this.commentData.likedNum = 0;
            // this.comments.push(this.commentData);
            let total_rating = this.file.rating * this.file.ratingNum;
            this.file.rating =
              (total_rating + this.commentData.rating) /
              (this.file.ratingNum + 1);
            this.file.rating = parseFloat(this.file.rating.toFixed(2));
            this.file.ratingNum += 1;

            this.commentData = {
              rating: 5,
              content: ""
            };

            this.$axios
              .get("/api/comments/file/" + this.file._id)
              .then(response => {
                // JSON responses are automatically parsed.
                if (response.status == 200) {
                  this.comments = response.data;
                  this.$forceUpdate();
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });

            this.$swal({
              title: "Success",
              text: "You have post a review!",
              type: "success"
            });
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    },
    likeComment(comment) {
      window.console.log("like comment event:", comment);
      this.$axios
        .get("/api/likes/", {
          params: { user_id: comment.user, comment_id: comment._id }
        })
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            window.console.log("liked successfully");
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log(
        "lost params(file data), sending request to backend.."
      );
      this.$axios
        .get("/api/files/" + this.$route.query.fileId)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            this.file = response.data;
            this.$axios
              .get("/api/comments/file/" + this.file._id, {
                params: { user_id: this.$store.getters.getUserId }
              })
              .then(response => {
                // JSON responses are automatically parsed.
                if (response.status == 200) {
                  this.comments = response.data;
                  this.$forceUpdate();
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
          }
        })
        .catch(err => {
          window.console.log(err.response);
          this.$axios
            .get("/api/comments/file/" + this.file._id)
            .then(response => {
              // JSON responses are automatically parsed.
              if (response.status == 200) {
                this.comments = response.data;
              }
            })
            .catch(err => {
              window.console.log(err.response);
            });
        });
    }
  }
};
</script>

<style scoped>
</style>
