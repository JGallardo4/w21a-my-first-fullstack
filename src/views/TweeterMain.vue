<template>
  <body>
    <Tweeter-header></Tweeter-header>
    <main>
      <main-display></main-display>
    </main>
  </body>
</template>

<script>
import TweeterHeader from "../components/TweeterHeader.vue";
import MainDisplay from "../components/MainDisplay.vue";

export default {
  name: "Tweeter-main",

  components: {
    TweeterHeader,
    MainDisplay,
  },

  beforeCreate() {
    this.$store.dispatch("checkLogin");
  },
};
</script>

<style lang="scss" scoped>
@mixin formReset() {
  input {
    font-size: inherit;
    font-size: calc(max(16px, 1em));
    font-family: inherit;
    padding: 0.25em 0.5em;
    background-color: #fff;
    border: 1px solid black;
    border-radius: 5px;
  }
  legend {
    padding: 0 0.5rem;
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

@media screen and (min-width: 769px) {
  //
}
</style>
