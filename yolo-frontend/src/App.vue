<template>
  <div id="app">
    <VideoStream />
  </div>
</template>

<script>
import VideoStream from './components/VideoStream.vue'

export default {
  name: 'App',
  components: {
    VideoStream
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
