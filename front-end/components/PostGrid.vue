<template>
  <section class="post-grid">
    <post v-for="(post, id) in posts" :key="id" class="post" :post="post">
    </post>
  </section>
</template>

<script>
import Post from "../components/Post.vue";

export default {
  name: "post-grid",
  props: {
    posts: {
      type: Array,
    },
  },
  components: {
    Post,
  },
};
</script>

<style lang="scss" scoped>
.post-grid {
  padding: 1rem;
  place-self: stretch;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
  gap: 2rem;
  place-items: stretch;

  .post {
    border: solid 1px black;
  }
}

@media screen and (max-width: 500px) {
  .post-grid {
    padding: 2px;
    gap: 2px;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  }
}
</style>
