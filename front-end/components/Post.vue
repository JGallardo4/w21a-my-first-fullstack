<template>
  <article class="post">
    <button
      v-if="userId == post.userId"
      @click="deletePost()"
      id="delete-button"
    >
      <div id="delete-icon"><font-awesome-icon icon="times" /></div>
    </button>

    <p id="post-content">{{ post.Content }}</p>

    <section id="post-info">
      <form @submit.prevent="editPost()" v-if="userId == post.User_Id">
        <router-link
          :to="{
            name: 'Edit',
            params: { postId: this.post.Id },
          }"
        >
          <button type="submit" id="edit-button" title="Edit this Post">
            <div id="edit-icon">
              <font-awesome-icon icon="pen" />
            </div>
          </button>
        </router-link>
      </form>

      <p id="post-author">{{ post.username }}</p>
      <p id="post-date">{{ post.Created_At }}</p>
    </section>
  </article>
</template>

<script>
export default {
  name: "Post",

  props: {
    post: {
      type: Object,
    },
  },

  computed: {
    loginToken() {
      return this.$store.getters.getLoginToken;
    },
    userId() {
      return this.$store.getters.getUserId;
    },
  },

  methods: {
    deletePost() {
      this.$store.dispatch("deletePost", {
        loginToken: this.loginToken,
        postId: this.post.postId,
      });

      this.$store.dispatch("refreshPosts");
    },

    editPost() {
      this.$store.dispatch("redirectAction", "edit");
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

.post {
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: 3rem 8rem 3rem auto;
  height: min-content;

  #delete-button {
    grid-column: 2;
    grid-row: 1;
    @include resetButton;
    padding: 1rem;

    &:hover {
      background-color: lightpink;
    }
  }

  #post-content {
    grid-column: 1 / 3;
    grid-row: 2;
    padding: 1rem;
    place-self: center;
  }

  #post-info {
    grid-column: 1 / 3;
    grid-row: 3;
    display: flex;
    justify-content: right;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
  }

  #edit-button {
    @include resetButton;
  }
}

@media screen and (max-width: 600px) {
  .post {
    #delete-button {
      padding: 10px;
    }
    #post-content {
      padding: 2px;
    }
  }
}
</style>
