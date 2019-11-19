<template>
  <div class="card overflow-auto shadow-sm h-100 w-100">
    <!-- project info dispaly -->
    <div v-if="project.title">
      <div class="card">
        <div class="card-header my-bg font-weight-bold">{{ project.title }}</div>
        <div class="card-body">
          <p class="text-left p-2">{{ project.description }}</p>
        </div>
        <!-- project files display start -->
        <div class="card mx-4 my-4" style="height:300px">
          <div class="card-header">Project Files:</div>
          <div class="card-body text-left overflow-auto">
            <div @click="clickFile(file)" :key="idx" v-for="(file, idx) in project.files">
              <div class="row file-row">
                <div class="col-6">
                  <span class="file-name mr">{{ handleFileName(file.name) }}</span>
                </div>
                <!-- project rating start -->
                <div class="col-6">
                  <div v-if="file.rating">
                    <star-rating
                      :inline="true"
                      :read-only="true"
                      :rating="file.rating"
                      :show-rating="false"
                      v-bind:increment="0.01"
                      v-bind:star-size="15"
                    ></star-rating>
                    <small class="ml-2">{{file.rating}}</small>
                  </div>

                  <!-- display text content when no rating data -->
                  <div v-if="!file.rating">
                    <small>No rating yet...</small>
                  </div>
                </div>
                <!-- project rating end -->
              </div>
            </div>
          </div>
        </div>
        <!-- project files display end -->
        <div class="card-footer p-1">
          <small>{{ project.createdTime }}</small>
        </div>
      </div>
    </div>
    <!-- project info dispaly end -->

    <!-- hint -->
    <div class="card h-100 shadow-sm" v-if="!project.title">
      <div class="card-body h-100">
        <p class="mt-4">Click a project to see more.</p>
      </div>
    </div>
    <!-- hint end -->
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "ProjectInfo",
  props: {
    project: Object
  },
  components: {
    StarRating
  },
  methods: {
    clickFile(file) {
      window.console.log("clicked file in ProjectInfo", file);
      // take user to the file page when user clicked a file
      this.$router.push({
        name: "file",
        query: { fileId: file._id },
        params: { file: file }
      });
    },
    handleFileName(fileName) {
      // return only first 18 characters of the file's name
      return fileName.substring(0, 18) + (fileName.length > 18 ? "..." : "")
    }
  },
};
</script>

<style scoped>
/* .file-name:hover {
  color: #9852f9;
} */

.file-row:hover {
  background-color: rgba(0, 0, 0, .03)
}
</style> 