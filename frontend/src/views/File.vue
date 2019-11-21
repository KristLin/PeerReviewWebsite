<template>
  <div class="container" style="padding-top:50px">
    <div class="row">
      <!-- file page left side start -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px">
        <!-- go back button start -->
        <div style="height:50px">
          <button class="my-back-btn form-control mb-2" @click="$router.go(-1)">
            <i class="fas fa-chevron-left"></i> Go Back
          </button>
        </div>
        <!-- go back button end -->

        <!-- file info display start -->
        <div style="height:500px">
          <div class="card h-100 shadow" v-if="!file"></div>
          <div class="card h-100 shadow" v-if="file">
            <div class="card-header my-bg font-weight-bold">{{ file.name }}</div>
            <div class="card-body overflow-auto">
              <highlight-code class="text-left" :lang="getLang(file.name)">{{ file.content }}</highlight-code>
            </div>
            <!-- file rating start -->
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
              <!-- show text content if the file has no rating data -->
              <small v-if="file.rating===0">This file hasn't received any rating yet...</small>
            </div>
            <!-- file rating end -->
          </div>
        </div>
        <!-- file info display end -->
      </div>
      <!-- file page left side end -->

      <!-- Loading -->
      <div class="col-lg-6 col-md-12 mb-4" style="padding-top: 100px" v-if="!hasFetchedData">
        <h4 class="my-4">Loading ...</h4>
        <b-spinner
          variant="secondary"
          style="width: 5rem; height: 5rem; font-size:2rem;"
          label="Loading..."
        ></b-spinner>
      </div>
      <!-- Loading end -->

      <!-- comments -->
      <div class="col-lg-6 col-md-12 mb-4" style="height:550px" v-if="hasFetchedData">
        <Comments :comments="comments" @likeComment="likeComment" />
      </div>
      <!-- comments end -->

      <!-- leave review -->
      <div class="card mx-auto shadow-sm mt-4" style="width:550px">
        <!-- user rating start -->
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
        <!-- user rating end -->

        <!-- user review content and submit button -->
        <div class="card-body">
          <textarea class="form-control mb-2" placeholder="Type your comment here." v-model="commentData.content" cols="30" rows="5"></textarea>
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
      // file's comments
      comments: [],
      // user's comment data
      commentData: {
        rating: 5,
        content: ""
      },
      // all required data has fetched or not
      // to decide when to show loading animation
      hasFetchedData: false
    };
  },
  methods: {
    // detect file's language based on the filename
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
    // post review function
    leaveReview() {
      // if user has not logged in yet, ask if user want to login
      if (!this.$store.getters.isLoggedIn) {
          this.$swal({
          title: "Confirm",
          text: "Log in required, do you want to login now?",
          type: "warning",
          showCancelButton: true,
          confirmButtonText: "Log in"
        }).then(result => {
          if (result.value) {
            this.$router.push({ name: "login" });
          }
        })
      }

      // if user is not logged in and not been taken to login page
      // the following code block can not be executed
      if (!this.$store.getters.isLoggedIn) {
        return;
      }

      // check if the review content is empty
      if (this.commentData.content === "") {
        this.$swal("Warnning", "You didn't input any content!", "warning");
        return;
      }

      // form the commentData based on user's input and user information
      this.commentData.user = this.$store.getters.getUserId;
      this.commentData.userName = this.$store.getters.getUserName;
      this.commentData.file = this.file._id;

      // post comment data to the backend server
      this.$axios
        .post("/api/comments/", this.commentData)
        .then(response => {
          if (response.status == 200) {
            // if the post request succeed, update the file's rating
            let total_rating = this.file.rating * this.file.ratingNum;
            this.file.rating =
              (total_rating + this.commentData.rating) /
              (this.file.ratingNum + 1);
            this.file.rating = parseFloat(this.file.rating.toFixed(1));
            this.file.ratingNum += 1;

            this.commentData = {
              rating: 5,
              content: ""
            };
            
            // get the updated file's comments data from backend
            this.$axios
              .get("/api/comments/file/" + this.file._id, {
                params: { user_id: this.$store.getters.getUserId }
              })
              .then(response => {
                if (response.status == 200) {
                  this.comments = response.data;
                  this.$swal({
                    title: "Success",
                    text: "You have post a review!",
                    type: "success"
                  })
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    },

    // liked comment action
    likeComment(comment) {
      window.console.log("like comment event:", comment);

      // post like data to backend server
      this.$axios
        .get("/api/likes/", {
          params: {
            user_id: this.$store.getters.getUserId,
            comment_id: comment._id
          }
        })
        .then(response => {
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
    // if the file data (in the route parameters) is lost
    // send request to backend to get the file data
    if (Object.keys(this.$route.params).length === 0) {
      window.console.log(
        "lost params(file data), sending request to backend.."
      );
      // request file data
      this.$axios
        .get("/api/files/" + this.$route.query.fileId)
        .then(response => {
          if (response.status == 200) {
            this.file = response.data;

            // get comments data
            this.$axios
              .get("/api/comments/file/" + this.file._id, {
                params: { user_id: this.$store.getters.getUserId }
              })
              .then(response => {
                if (response.status == 200) {
                  this.comments = response.data;
                  this.hasFetchedData = true;
                }
              })
              .catch(err => {
                window.console.log(err.response);
              });
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    // if the page has the file's data, only need to request the comments data
    } else {
      // get comments data
      this.$axios
        .get("/api/comments/file/" + this.file._id, {
          params: { user_id: this.$store.getters.getUserId }
        })
        .then(response => {
          if (response.status == 200) {
            this.comments = response.data;
            this.hasFetchedData = true;
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  }
};
</script>

<style scoped>
</style>
