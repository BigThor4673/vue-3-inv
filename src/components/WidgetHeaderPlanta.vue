<template>
  <div class="row pl-2 mb-4 border-bottom border-dark">
    <!-- banco -->
    <div class="col-sm-6">
      <h6 class="float-left font-weight-bolder">{{ banco }}</h6>
    </div>
    <!-- genetica -->
    <div class="col-sm-6">
      <h5><span class="badge badge-light float-right p-2">{{ genetica }}</span></h5>
    </div>
    <!-- nombre -->
    <div class="col-sm-12">
      <h1>{{ nombre }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "header-planta-widget",
  props: ["banco", "genetica", "nombre"],
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
.widgetsLeft .linea3.encendida {
  color: rgb(255 255 0) !important;
}

.widgetsLeft .linea3.edad {
  color: rgb(68, 102, 227) !important;
}
</style>
