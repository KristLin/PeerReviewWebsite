<template>
  <div class="container">
    <h1>Your Major: {{ $store.getters.getUserMajor }}</h1>
    <div class="w-50 my-4 mx-auto">
      <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
    </div>

    <div class="row">
      <div class="col-lg-7 col-md-12 md-4" style="height:500px">
        <ProjectList :projects="filterProjects(projects)" @clickProject="clickProject" />
      </div>
      <div class="col-lg-5 col-md-12 md-4" style="height:500px">
        <ProjectInfo :project="chosenProject" />
      </div>
    </div>
  </div>
</template>

<script>
import ProjectList from "@/components/ProjectList.vue";
import ProjectInfo from "@/components/ProjectInfo.vue";

export default {
  name: "search",
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
          description:
            "A simple frontend of peer review website. A simple frontend of peer review website. A simple frontend of peer review website.",
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
            },
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
            },
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
            },
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
            },
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
            },
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
              mark: 0
            }
          ]
        },
        {
          id: "3",
          name: "My sad story",
          description: "A sad story...",
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
                "He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...He was warking on a web project...\nAnd he went crazy...",
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
    },
    filterProjects(projects) {
      let keyword = this.searchData.keyword.toLowerCase();
      var filteredProjects = projects.filter(function(project) {
        return (
          project.name.toLowerCase().includes(keyword) ||
          project.description.toLowerCase().includes(keyword)
        );
      });
      return filteredProjects;
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
