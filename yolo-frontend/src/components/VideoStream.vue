<template>
  <div id="app">
    <h1>Live Streaming Video</h1>
    <img :src="videoFeedUrl" alt="Live Stream" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoFeedUrl: 'http://localhost:5000/video_feed'
    };
  }
};
</script>

<style>
#app {
  text-align: center;
}
img {
  width: 80%;
  height: auto;
  border: 2px solid #000;
}
</style>
