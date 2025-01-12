<template>
  <!-- <div class="row widgetsRight pl-md-4 pt-md-2 my-md-4 shadow rounded"> -->
  <div class="row widgetsRight shadow rounded mb-md-4 py-md-2 mx-1 py-2">
      <div class="col-sm-4 my-auto px-0">
          <img :src="imagenUrl" class="rounded img-fluid mx-auto d-block w-75 imgWidget"
              alt="humedad suelo">
      </div>
      <div class="col-sm-8 pl-sm-0">
          <!-- <p class="linea1 mb-0 h2"><strong>{{ linea1 }}</strong></p> -->
          <p class="linea1 mb-0 h4 font-weight-bold mx-auto text-center">{{ linea1 }}</p>
          <!-- <p class="linea2 text-monospace h5">{{ linea2 }}</p> -->
          <p class="linea2 d-none d-sm-block text-center"><small class="text-monospace">{{ linea2 }}</small></p>
          <small class="linea2 d-block d-sm-none text-center text-monospace minitexto">{{ linea2 }}</small>
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

  .minitexto {
    font-size: 0.6rem;
  }
</style>
