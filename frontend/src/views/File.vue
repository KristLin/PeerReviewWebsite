<template>
  <div class="container file-page">
    <div class="row">
      <div class="col-5">
        <div class="card" style="height: 400px;">
          <div class="card-header">File.txt</div>
          <div class="card-body">
            <p>File Content</p>
          </div>
        </div>
      </div>
      <div class="col-7">
        <div class="overflow-auto" style="height: 400px;">
          <div class="card mb-4">
            <div class="card-header">Comments</div>
            <div class="card-body">
              <div class="row">
                <div class="col-4">
                  <p class="form-control">User Name</p>
                </div>
                <div class="col-8">
                  <p class="form-control">Comment Content</p>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-header">Comments</div>
            <div class="card-body">
              <div class="row">
                <div class="col-4">
                  <p>User Name</p>
                </div>
                <div class="col-8">
                  <p>Comment Content</p>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-header">Comments</div>
            <div class="card-body">
              <div class="row">
                <div class="col-4">
                  <p>User Name</p>
                </div>
                <div class="col-8">
                  <p>Comment Content</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
    };
  },
  methods: {
  }
};
</script>

<style scoped>
.file-page {
  margin-top: 50px;
  margin-bottom: 100px;
}

.my-btn {
  border: none;
  background-color: #c299fc;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #9852f9;
  color: white;
}
</style>
