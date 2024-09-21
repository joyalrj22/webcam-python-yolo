<template>
  <div id="app">
    <img :key="imgKey" :src="videoFeedUrl" alt="Live Stream" />
    <div class="button-set">
        <b-button variant="primary" @click="filterType='NONE'"> No Filter </b-button>
        <b-button variant="primary" @click="filterType='BOX_FILTER'"> Box Filter </b-button>
        <b-button variant="primary" @click="filterType='GAUSSIAN_FILTER'"> Gaussian Filter </b-button>
        <b-button variant="primary" @click="filterType='MEDIAN_FILTER'"> Median Filter </b-button>
        <b-button variant="primary" @click="filterType='BILATERAL_FILTER'"> Bilateral Filter </b-button>
        <b-button variant="primary" @click="filterType='OBJECT_DETECTION'"> Object Detection </b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imgKey: 0,
      filterType: 'NONE'
    };
  },
  computed: {
    videoFeedUrl() {
        return `http://localhost:5000/video_feed?type=${this.filterType}`
    }
  },
  watch: {
    filterType() {
        this.imgKey += 1
    }
  }
};
</script>

<style>
#app {
  text-align: center;
  position: absolute;
  top: 10px;
  left: 10px;
}
img {
  width: 100%;
  height: 100%;
  border: 2px solid #000;
}

.image-container {
  position: relative;
  display: inline-block;
}
</style>
