<template>
  <div style="height: 500px;">
    <!-- project info dispaly -->
    <div class="overflow-auto shadow-sm h-100" v-if="project.name">
      <div class="card h-100">
        <div class="card-header my-bg font-weight-bold">{{ project.name }}</div>
        <div class="card-body">
          <p>{{ project.description }}</p>
        </div>
        <div class="card mx-4 my-4 h-50">
          <div class="card-header">File List:</div>
          <div class="card-body text-left overflow-auto">
            <div @click="clickFile(file)" :key="idx" v-for="(file, idx) in project.files">
              <div class="row">
                <div class="col-6">
                  <span class="file-name mr-4">{{ file.name }}</span>
                </div>
                <div class="col-6">
                  <div class="has-mark" v-if="file.mark>0">
                    <star-rating
                      :inline="true"
                      :read-only="true"
                      :rating="file.mark"
                      :show-rating="false"
                      v-bind:increment="0.01"
                      v-bind:star-size="15"
                    ></star-rating>
                    <small class="ml-2">{{file.mark}}</small>
                  </div>
                  <div class="no-mark" v-if="file.mark===0">
                    <small>No mark yet...</small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="card-footer p-1">
          <small>{{ project.createdTime }}</small>
        </div>
      </div>
    </div>
    <!-- project info dispaly end -->

    <!-- hint -->
    <div class="card h-100 shadow-sm" v-if="!project.name">
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
      this.$router.push({
        name: "file",
        query: { fileId: file.id },
        params: { file: file }
      });
    }
  }
};
</script>

<style scoped>
.file-name:hover {
  color: #9852f9;
}
</style> 