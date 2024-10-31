<template>
  <div class="row pl-2 mb-4 border-bottom border-dark">
    <div class="col-sm-12">
      <div class="row">
        <div class="col-6">
          <h6 class="font-weight-bolder mb-0 text-dark">{{ banco }}</h6>
        </div>
        <div class="col-6">
          <h5><span class="badge badge-light float-right p-2 text-success">{{ genetica }}</span></h5>
        </div>
      </div>
      <div class="row">
        <h1 class="nombre-planta font-weight-bold">{{ nombre }}</h1>
      </div>
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

  .nombre-planta{
    font-family: Georgia, serif !important;
    font-size: 3rem;
  }
</style>
