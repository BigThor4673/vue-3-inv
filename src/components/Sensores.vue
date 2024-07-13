<template>
  <div class="list row">
    <div class="col-md-12">
      <h3>Sensores</h3>
    </div>
    <div class="col-md-4">
      <h4>Humedad Tierra</h4>
      <strong>{{ sensorHumedadTierra }}</strong>
    </div>
    <div class="col-md-4">
      <h4>Humedad Ambiente</h4>
      <strong>{{ sensorHumedadAmbiente }}</strong>
    </div>
    <div class="col-md-4">
      <h4>Luz</h4>
      <strong>{{ sensorLuz }}</strong>
    </div>
  </div>
</template>

<script>
import SensoresService from "../services/SensoresService";

export default {
  name: "sensores",
  data() {
    return {
      sensorHumedadTierra: null,
      sensorHumedadAmbiente: null,
      sensorLuz: null,
      unsubscribe: null
    };
  },
  methods: {
    onDataChange(items) {
      items.forEach((item) => {
        //FIXME: Corregir la llamada a la colección para que también lea los metadatos raza, banco y germinacion.
        let data = item.data();
        if(item.id == "humedad-tierra"){
          this.sensorHumedadTierra = data.valor;
        }
        else if(item.id == "humedad-ambiente"){
          this.sensorHumedadAmbiente = data.valor;
        }
        else if(item.id == "luz"){
          this.sensorLuz = data.valor;
        }
      });
    },
  },
  mounted() {
    this.unsubscribe = SensoresService.getAll().onSnapshot(this.onDataChange);
  },
  beforeUnmount() {
    this.unsubscribe();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
