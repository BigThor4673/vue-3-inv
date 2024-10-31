<template>
  <div class="row widgetsLeft mb-md-4 mt-md-5 pb-md-4 pt-md-4 text-center">
    <div class="col-sm-12 p-0">
      <p class="linea1 m-0 h4"><strong>{{ linea1 }}</strong></p>
    </div>
    <div class="col-sm-12 p-0">
      <!-- <p class="linea2 m-0 font-weight-bold">{{ linea2 }}</p> -->
      <small class="m-0 font-weight-bold">{{ linea2 }}</small>
    </div>
    <div class="col-sm-12 p-0">
      <p class="linea3 m-0 font-weight-bold" :class="clase">{{ linea3 }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "indicador-widget",
  props: ["linea1", "linea2", "linea3", "clase"],
  data() {
    return {
    };
  },
  computed: {
  },
  mounted() {
  },
};
</script>

<style>
/* Agrega tus estilos aquí */
  .widgetsLeft .linea3.encendida{
    color: rgb(255 255 0) !important;
  }

  .widgetsLeft .linea3.apagada{
    color: #6c757d !important;
  }

  .widgetsLeft .linea3.edad{
    color: rgb(68, 102, 227) !important;
  }
</style>
