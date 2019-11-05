<template>
  <div class="container" style="width:500px">
    <ul class="list-group">
      <li class="list-group-item active">User Points Ranking</li>
      <li
        class="list-group-item list-group-item-action"
        :key="idx"
        v-for="(user, idx) in top10"
      >{{ user.name }}({{ user.major }}): {{ user.points }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "rank",
  data() {
    return {
      top10: [
        {
          name: "Krist",
          points: 1020,
          major: "CSE"
        },
        {
          name: "Jack",
          points: 890,
          major: "Finance"
        },
        {
          name: "Janis",
          points: 780,
          major: "CSE"
        },
        {
          name: "Krist",
          points: 1020,
          major: "CSE"
        },
        {
          name: "Jack",
          points: 890,
          major: "Finance"
        },
        {
          name: "Janis",
          points: 780,
          major: "CSE"
        },
        {
          name: "Krist",
          points: 1020,
          major: "CSE"
        },
        {
          name: "Jack",
          points: 890,
          major: "Finance"
        },
        {
          name: "Janis",
          points: 780,
          major: "CSE"
        }
      ]
    };
  }
};
</script>

<style scoped>
</style>
