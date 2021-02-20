<template>
  <section id="new-post">
    <form action="" id="post__form" @submit.prevent="updatePost()">
      <fieldset id="post__fieldset">
        <legend>Edit Post</legend>

        <p id="post-content">
          <textarea
            rows="5"
            cols="40"
            name="post-content"
            v-model="input"
          ></textarea>
        </p>

        <p id="character-count" :class="{ overLimit: isOverLimit }">
          {{ totalCharacters }} / 140 characters
        </p>

        <section id="buttons">
          <router-link to="/">
            <button type="submit" id="cancel-button">
              <span id="cancel-icon">
                <font-awesome-icon icon="undo" />
              </span>

              <span>Cancel</span>
            </button>
          </router-link>

          <button
            :disabled="isOverLimit"
            :class="{ disabled: isOverLimit }"
            type="submit"
            id="submit-button"
          >
            Edit Post
          </button>
        </section>
      </fieldset>
    </form>
  </section>
</template>

<script>
export default {
  name: "edit-post",

  data: function() {
    return {
      input: "",
    };
  },

  created: function() {
    this.input = this.$store.getters.getAllPosts.find(
      (post) => post.tweetId == this.postId
    ).content;
  },

  props: {
    postId: {
      type: Number,
    },
  },

  computed: {
    totalCharacters() {
      return this.input.length;
    },

    isOverLimit() {
      return this.input.length > 200;
    },
  },

  methods: {
    updatePost() {
      this.$axios
        .patch("/posts", {
          loginToken: this.$store.getters.getLoginToken,
          postId: this.postId,
          content: this.input,
        })
        .then(() => this.$store.dispatch("redirect", "/"))
        .catch((response) => console.log(response));
    },
  },
};
</script>

<style lang="scss" scoped>
@mixin formReset() {
  legend {
    padding: 0 0.5rem;
  }
  input {
    font-size: 16px;
    font-size: calc(max(16px, 1em));
    font-family: inherit;
    padding: 0.25em 0.5em;
    background-color: #fff;
    border: 1px solid black;
    border-radius: 5px;
    width: 100%;

    &:not(textarea) {
      line-height: 1;
      height: 2.25rem;
    }
  }
}

@mixin resetButton() {
  background: none;
  color: inherit;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}

@include formReset;

#new-post {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: url("https://source.unsplash.com/random");
  background-size: cover;
  #post__form {
    padding: 0.5rem;
    border-radius: 10px;
    background-color: white;

    #post__fieldset {
      padding: 1rem;
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr auto;
      gap: 1rem;
      border-radius: 10px;
      border-style: solid;
      border-width: 1px;
      border-color: black;

      fieldset {
        border: 0;
        display: grid;
      }

      textarea {
        padding: 1rem;
        font-size: 15pt;
      }

      #character-count {
        justify-self: right;
        &.overLimit {
          color: red;
        }
      }

      #buttons {
        display: flex;
        justify-content: space-between;
        #submit-button,
        #cancel-button {
          grid-row: 3;
          @include resetButton;
          border: 1px solid black;
          background-color: black;
          color: white;
          font-weight: bold;
          border-radius: 10px;
          place-self: center;
          padding: 1rem 1.5rem;
          &:hover {
            background-color: white;
            color: black;
          }
          &.disabled {
            background-color: gray;
            color: black;
            cursor: not-allowed;
          }
        }
      }

      #error-message {
        color: darkred;
      }
    }
  }
}

@media screen and (max-width: 500px) {
  #new-post {
    #post__form {
      padding: 0;
      #post__fieldset {
        padding: 3px 0 3px 0;
        gap: 2px;
        textarea {
          padding: 2px;
          font-size: 13pt;
          width: 97vw;
          height: 16rem;
        }
      }
    }
  }
}
</style>
