<template>
    <div class="container-fluid">
    <div class="card w-100 h-50 mx-auto mt-2 shadow" id="cardCalendario">
    <div class="card-body">
      <FullcalendarWidget/>
    </div>
    </div>
    </div>

</template>

<script>
import FullcalendarWidget from "./FullcalendarWidget.vue";
export default {
  name: "calendario-widget",
  components: {
    FullcalendarWidget
  },
  data() {
    return {
    };
  },
  methods: {

  },
  mounted() {

  },
  beforeUnmount() {

  }
};
</script>

<style>
</style>
