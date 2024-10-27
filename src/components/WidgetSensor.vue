<template>
  <div class="row widgetsRight pl-4 pt-2 my-4 shadow rounded">
      <div class="col-sm-4 my-auto px-0">
          <img :src="imagenUrl" class="rounded mx-auto d-block w-100 imgWidget"
              alt="humedad suelo">
      </div>
      <div class="col-sm-8 pl-0">
          <p class="linea1 mb-0 h2"><strong>{{ linea1 }}</strong></p>
          <p class="linea2 text-monospace"><span>{{ linea2 }}</span></p>
      </div>
  </div>
</template>

<script>
export default {
  name: "sensor-widget",
  props: ["linea1", "linea2", "imagen"],
  data() {
    return {
      imgHumedadSuelo: require('../assets/images/sensors/humedad-suelo.png') ,
      imgHumedadAmbiente: require('../assets/images/sensors/humedad-ambiente.png') ,
      imgTempAmbiente: require('../assets/images/sensors/temperatura-ambiente.png') 
    };
  },
  computed: {
    imagenUrl() {
      switch (this.imagen) {
        case 'humedad-suelo':
          return this.imgHumedadSuelo;
        case 'temp-ambiente':
          return this.imgTempAmbiente;
        case 'humedad-ambiente':
          return this.imgHumedadAmbiente;
        default:
          return this.imgTempAmbiente;
      }
    }
  },
  mounted() {
  },
};
</script>

<style>
/* Agrega tus estilos aquí */
  .widgetsRight { 
    background-color: rgba(255, 255, 255, .5); 
  }
</style>
