<template>
  <div class="overflow-auto h-100">
    <div class="card mb-4 shadow-sm" :key="idx" v-for="(comment, idx) in comments">
      <div class="card-body">
        <!-- user name & comment content -->
        <div class="row">
          <div class="col-4">
            <p>{{ comment.user }}</p>
          </div>
          <div class="col-8">
            <p class="text-left">{{ comment.content }}</p>
          </div>
        </div>
        <!-- user name & comment content end -->

        <!-- like button & like num -->
        <div class="row">
          <div class="col-8"></div>
          <div class="col-2 text-right">
            <i
              class="far fa-thumbs-up unliked-icon"
              @click="like(comment)"
              v-if="!comment.hasLiked"
            ></i>
            <i class="fas fa-thumbs-up liked-icon" @click="unLike(comment)" v-if="comment.hasLiked"></i>
          </div>
          <div class="col-2 text-left">
            <small class="font-weight-bold">{{ comment.likedNum }}</small>
          </div>
        </div>
        <!-- like button & like num end -->
      </div>
      <div class="card-footer p-1">
        <small>{{ comment.postTime }}</small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Comments",
  props: {
    comments: Array
  },
  methods: {
    like(comment) {
      comment.hasLiked = true;
      comment.likedNum += 1;
    },
    unLike(comment) {
      comment.hasLiked = false;
      comment.likedNum -= 1;
    }
  }
};
</script>

<style scoped>
.liked-icon {
  color: #f0134d;
}

.unliked-icon:hover {
  color: #f0134d;
}
</style> 