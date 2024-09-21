<template>
  <div id="app">
    <img :key="imgKey" :src="videoFeedUrl" alt="Live Stream" />
    <div class="button-set">
        <b-button :variant="filterTypeStyle('NONE')" @click="filterType='NONE'"> <b-icon icon="card-image"/> No Filter </b-button>
        <b-button :variant="filterTypeStyle('BOX_FILTER')" @click="filterType='BOX_FILTER'"> <b-icon icon="bounding-box-circles"/> Box Filter </b-button>
        <b-button :variant="filterTypeStyle('GAUSSIAN_FILTER')" @click="filterType='GAUSSIAN_FILTER'"> <b-icon icon="bezier"/> Gaussian Filter </b-button>
        <b-button :variant="filterTypeStyle('MEDIAN_FILTER')" @click="filterType='MEDIAN_FILTER'"> <b-icon icon="border-middle"/> Median Filter </b-button>
        <b-button :variant="filterTypeStyle('BILATERAL_FILTER')" @click="filterType='BILATERAL_FILTER'"> <b-icon icon="bezier-2"/> Bilateral Filter </b-button>
        <b-button :variant="filterTypeStyle('OBJECT_DETECTION')" @click="filterType='OBJECT_DETECTION'"> <b-icon icon="person"/> Object Detection </b-button>
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
  },
  methods: {
    filterTypeStyle(mode) {
        return mode === this.filterType ? "primary" : "secondary"
    }
  }
};
</script>

<style>
#app {
    width: 100%;
    height: 100%;
    text-align: center;
    position: absolute;
    top: 10px;
    left: 10px;
}

.image-container {
    width: 100%;
    height: 100%;
    position: relative;
    display: inline-block;
}

.btn {
    margin-left: 3px;
    margin-top: 1px;
}
</style>
