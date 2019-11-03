<template>
  <div class="container">
    <h1>My Projects</h1>
    <p class="text-right">Rest Top Times: 10</p>
    <div class="w-50 my-2 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div>

    <button
      class="my-btn w-50 mx-auto my-4 form-control"
      @click="$router.push({name: 'createProject'})"
    >Create New Project</button>
    <hr />

    <div class="row">
      <!-- project list -->
      <div class="col-lg-7 col-md-12 md-4" style="height:500px">
        <ProjectList :projects="projects" @clickProject="clickProject" />
      </div>
      <!-- project list end -->

      <!-- top up button & project info -->
      <div class="col-lg-5 col-md-12 md-4">
        <div class="row" style="height:50px">
          <button class="form-control btn btn-warning" v-if="chosenProject.name">Top Up!</button>
          <p class="form-control" v-if="!chosenProject.name">Top Up!</p>
        </div>
        <div class="row" style="height:450px">
          <ProjectInfo :project="chosenProject" />
        </div>
      </div>
      <!-- top up button & project info end -->
    </div>
  </div>
</template>

<script>
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "myProjects",
  components: {
    ProjectList,
    ProjectInfo
  },
  data() {
    return {
      searchData: {
        keyword: "",
        orderType: ""
      },
      projects: [
        {
          id: "1",
          name: "Peer Review Frontend",
          description: "A simple frontend of peer review website",
          major: "CSE",
          createdTime: "2019-10-29 16:00:00",
          files: [
            {
              id: "1",
              name: "index.html",
              content: "<h1>Hello World</h1>\n<h1>Bye World</h1>",
              mark: 3.8
            },
            {
              id: "2",
              name: "index.css",
              content: "h1{\n\tcolor: blue;\n}",
              mark: 3.5
            }
          ]
        },
        {
          id: "2",
          name: "Peer Review Backend",
          description: "A good backend design for peer review website",
          major: "CSE",
          createdTime: "2019-10-31 17:30:00",
          files: [
            {
              id: "3",
              name: "app.py",
              content: 'print("hello world")\nprint("bye world")',
              mark: 4.0
            },
            {
              id: "4",
              name: "database.py",
              content: 'print("hello!!")\nprint("bye!!")',
              mark: 4.7
            }
          ]
        },
        {
          id: "3",
          name: "Project 3",
          description: "description of project 3",
          major: "Literature",
          createdTime: "2019-11-01 12:00:00",
          files: [
            {
              id: "5",
              name: "part1.txt",
              content: "Once upon a time...\nThere is a web developer...",
              mark: 3.8
            },
            {
              id: "6",
              name: "part2.txt",
              content:
                "He was warking on a web project...\nAnd he went crazy...",
              mark: 2.9
            }
          ]
        }
      ],
      chosenProject: {}
    };
  },
  methods: {
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    }
  }
};
</script>

<style scoped>
</style>
