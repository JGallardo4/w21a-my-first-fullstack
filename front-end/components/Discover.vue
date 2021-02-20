<template>
  <section id="discover">
    <button @click="refresh()" id="refresh-button">Refresh</button>

    <post-grid :posts="posts"></post-grid>
  </section>
</template>

<script>
import PostGrid from "../components/PostGrid.vue";

export default {
  name: "discover",

  computed: {
    posts() {
      return this.$store.getters.getAllPosts;
    },
  },

  methods: {
    refresh() {
      this.$store.dispatch("refreshPosts");
    },
  },

  components: {
    PostGrid,
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

#discover {
  grid-template-rows: auto 1fr;
  #refresh-button {
    justify-self: right;
    @include resetButton;
    padding: 1rem;
    border-left: solid 1px black;
    border-bottom: solid 1px black;

    &:hover {
      background-color: lightgreen;
    }
  }
}
</style>
