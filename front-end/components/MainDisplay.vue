<template>
  <section id="main-display">
    <section id="tabs-container">
      <div id="tabs">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-button', { active: currentTab === tab }]"
          v-on:click="currentTab = tab"
        >
          {{ tab }}
        </button>
      </div>

      <component :is="currentTabComponent" class="tab"></component>
    </section>
  </section>
</template>

<script>
import MyPosts from "../components/MyPosts.vue";
import Discover from "../components/Discover.vue";
import NewPost from "../components/NewPost.vue";

export default {
  components: {
    MyPosts,
    Discover,
    NewPost,
  },

  name: "main-display",

  data: function () {
    return {
      currentTab: "My Posts",
      tabs: ["My Posts", "Discover", "New Post"],
    };
  },

  computed: {
    currentTabComponent() {
      return this.currentTab.toLowerCase().split(" ").join("-");
    },
  },
};
</script>

<style lang="scss" scoped>
@mixin resetButton() {
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}

#main-display {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto 1fr;
  padding: 2rem;
  gap: 1rem;
}

#tabs-container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto 1fr;
  border-style: solid;
  border-width: 1px;
  border-color: black;

  #tabs {
    grid-row: 1;
    display: flex;
    justify-content: left;
    border-bottom: solid 1px black;
    button {
      @include resetButton;
      padding: 1rem;
      border-right: solid 1px black;

      &:hover {
        background-color: gainsboro;
      }

      &.active {
        background-color: lightblue;
      }
    }
  }

  .tab {
    grid-row: 2;
    min-height: 50vh;
    display: grid;
  }
}

@media screen and (max-width: 600px) {
  #main-display {
    padding: 2px;
    gap: 2px;
  }
}
</style>
