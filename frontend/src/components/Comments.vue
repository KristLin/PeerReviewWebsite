<template>
<div class="h-100 w-100">
  <div class="overflow-auto h-100 w-100 border-top border-bottom" v-if="comments.length > 0">
    <div class="card comment-card mb-4 shadow-sm" :key="idx" v-for="(comment, idx) in comments">
      <div class="card-body pb-0">
        <!-- user name & comment content -->
        <div class="row">
          <div class="col-3">
            <div class="circle mx-auto">{{ comment.userName }}</div>
          </div>
          <div class="col-9">
            <p class="text-left comment-content border p-2" style="height:100px">{{ comment.content }}</p>
          </div>
        </div>
        <!-- user name & comment content end -->
      </div>
      <div class="card-footer">
        <div class="row">
          <div class="col-8 text-left">
            <small>{{ comment.createdTime }}</small>
          </div>

          <!-- like button & like num -->
          <div class="col-2 text-right">
            <i
              class="far fa-thumbs-up unliked-icon zoom"
              @click="like(comment)"
              v-if="!comment.hasLiked"
            ></i>
            <i class="fas fa-thumbs-up liked-icon zoom" @click="unLike(comment)" v-if="comment.hasLiked"></i>
          </div>
          <div class="col-2 text-left">
            <small class="unliked-num"  v-if="!comment.hasLiked">{{ comment.likedNum }}</small>
            <small class="liked-num" v-if="comment.hasLiked">{{ comment.likedNum }}</small>
          </div>
        </div>
        <!-- like button & like num end -->
      </div>
    </div>
  </div>

  <div class="card border h-100 w-100" v-if="comments.length === 0">
    <h5 style="margin-top:100px">This file has no comment yet...</h5>
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
.circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  color: #fff;
  line-height: 80px;
  text-align: center;
  background: rgba(0, 0, 0, .25);
  font-weight: bold;
  margin-top: 10px;
}

.comment-card:hover .card-header {
  background-color: #b281f8;
}
.comment-card:hover .card-body {
  background-color: rgba(0, 0, 0, .01)
}
.comment-card:hover .card-footer {
  background-color: rgba(0, 0, 0, .045)
}
.comment-card:hover .circle {
  background-color: rgba(0, 0, 0, .4)
}

.comment-content {
  font-size: 14px;
}

.liked-icon {
  color: #e0245e;
}

.unliked-icon {
  color: grey;
}

.unliked-icon:hover {
  color: #e0245e;
}

.liked-num {
  color: #e0245e;
  font-weight: bold;
}

.unliked-num {
  color: grey;
}
</style> 