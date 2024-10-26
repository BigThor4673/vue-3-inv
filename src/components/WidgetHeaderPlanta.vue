<template>
  <div class="row">
    <!-- banco -->
    <div class="col-sm-6">
      <h6 class="float-left">{{ banco }}</h6>
    </div>
    <!-- genetica -->
    <div class="col-sm-6">
      <span class="badge badge-light float-right mr-4">{{ genetica }}</span>
    </div>
    <!-- nombre -->
    <div class="col-sm-12">
      <h3>{{ nombre }}</h3>
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
