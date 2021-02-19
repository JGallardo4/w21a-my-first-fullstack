<template>
  <section id="my-tweets">
    <button @click="refreshLikedTweets()" id="refresh-button">
      Refresh
    </button>

    <tweet-grid :tweets="likedTweets"></tweet-grid>
  </section>
</template>

<script>
import TweetGrid from "../components/TweetGrid.vue";

export default {
  name: "my-liked-tweets",

  data: function() {
    return {
      likedTweets: [],
    };
  },

  computed: {
    tweets() {
      return this.$store.getters.getAllTweets.filter((tweet) =>
        this.$store.getters.getFollows.includes(tweet.userId)
      );
    },
  },

  mounted() {
    this.refreshLikedTweets();
  },

  methods: {
    refreshLikedTweets() {
      this.$axios
        .request({
          url: "/tweet-likes",
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD",
          },
        })
        .then((response) => {
          if (response.status === 200) {
            var ids = response.data
              .filter((tweet) => tweet.userId == this.$store.getters.getUserId)
              .map((tweet) => tweet.tweetId);

            this.likedTweets = this.$store.getters.getAllTweets.filter(
              (tweet) => ids.includes(tweet.tweetId)
            );
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  components: {
    TweetGrid,
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

#my-tweets {
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
