<template>
  <div class="row widgetsRight">
      <div class="col-sm-4">
          <img :src="imagenUrl" class="rounded mx-auto d-block w-100 imgWidget"
              alt="humedad suelo">
      </div>
      <div class="col-sm-8">
          <p class="linea1"><strong>{{ linea1 }}</strong></p>
          <p class="linea2"><span>{{ linea2 }}</span></p>
      </div>
  </div>
</template>

<script>
export default {
  name: "sensor-widget",
  props: ["linea1", "linea2", "imagen"],
  data() {
    return {
      imgHumedadSuelo: require('../assets/vectors/humedad_suelo.svg') ,
      imgTempAmbiente: require('../assets/vectors/temp_ambiental.svg') 
    };
  },
  computed: {
    imagenUrl() {
      switch (this.imagen) {
        case 'humedad':
          return this.imgHumedadSuelo;
        case 'ambiente':
          return this.imgTempAmbiente;
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
</style>
