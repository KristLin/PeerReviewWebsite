<template>
  <div class="container">
    <h1>Your Major: {{ $store.getters.getUserMajor }}</h1>
    <SearchInput :searchData="searchData" @searchRequest="searchProject" />

    <div class="row">
      <div class="col-7">
        <ProjectList :projects="projects" @clickProject="clickProject" />
      </div>
      <div class="col-5">
        <ProjectInfo :project="chosenProject" />
      </div>
    </div>
  </div>
</template>

<script>
import SearchInput from "@/components/SearchInput.vue";
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "search",
  components: {
    SearchInput,
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
    searchProject() {
      window.console.log(this.searchData);
    },
    clickProject(project) {
      window.console.log("received clicked project from ProjectList", project);
      this.chosenProject = project;
    }
  },
  created() {
    // test get request to the backend
    // this.$axios
    //     .get("/api/test/")
    //     .then(response => {
    //       this.resData = response.data;
    //       window.console.log(this.resData)
    //     })
    //     .catch(err => {
    //       window.console.log(err.response);
    //     });
    // test post request to the backend
    // this.$axios
    //   .post("/api/test/", {"num": 2, "float": 3.35, "str": "2019-10-31"})
    //   .then(response => {
    //     window.console.log(response.data);
    //   })
    //   .catch(err => {
    //     window.console.log(err.response);
    //   });
  }
};
</script>

<style scoped>
</style>
