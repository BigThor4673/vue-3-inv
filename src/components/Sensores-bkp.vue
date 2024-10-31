<template>
  <div class="card w-100 mx-auto mt-2 shadow">
    <div class="card-body">
      <div class="list row">
        <div class="col-md-12">
          <h3>Sensores</h3>
        </div>
        <div class="col-md-4">
          <h4>Humedad Tierra</h4>
          <strong>{{ sensorHumedadSuelo }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Humedad Ambiente</h4>
          <strong>{{ sensorHumedadAmbiente }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Temperatura Ambiente</h4>
          <strong>{{ sensorTemperaturaAmbiente }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Luz</h4>
          <strong>{{ sensorLuz }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Luz Update</h4>
          <strong>{{ sensorLuzFecha }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Nombre</h4>
          <strong>{{ plantaData.nombre }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Banco</h4>
          <strong>{{ plantaData.banco }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Tipo</h4>
          <strong>{{ plantaData.tipo }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Tipo Planta</h4>
          <strong>{{ plantaData.tipo_planta }}</strong>
        </div>
        <div class="col-md-4">
          <h4>Fecha Germinación</h4>
          <strong>{{ plantaData.fecha_germinacion ? plantaData.fecha_germinacion.toDate().toLocaleDateString() : null }}</strong>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { db } from "../firebase";

export default {
  name: "sensores",
  data() {
    return {
      unsubscribeDocument: null,
      unsubscribeSensores: null,
      sensorHumedadSuelo: null,
      sensorTemperaturaAmbiente: null,
      sensorHumedadAmbiente: null,
      sensorLuz: null,
      sensorLuzFecha: null,
      plantaData: {
        nombre: null,
        tipo: null, 
        tipo_planta: null,
        banco: null,
        fecha_germinacion: null
      },
    };
  },
  methods: {
    fetchData() {
      try {
        const docRef = db.collection('inv-data').doc('Inv-001').collection('maceteros').doc('ma-z01');
        // Verificación del documento principal
        this.unsubscribeDocument = docRef.onSnapshot(docSnapshot => {
          if (docSnapshot.exists) {
            console.log("Documento encontrado:", docSnapshot.data());
            this.plantaData = docSnapshot.data();
          } else {
            console.log("El documento no existe");
          }
        }, error => {
          console.error("Error al obtener el documento:", error);
        });

        // Verificación de la colección "sensores"
        this.unsubscribeSensores = docRef.collection('sensores').onSnapshot(sensoresSnapshot => {
          sensoresSnapshot.forEach(doc => {
            let itemData = doc.data();
            if(doc.id == "humedad-ambiente"){
              this.sensorHumedadAmbiente = itemData.valor;
            }
            else if(doc.id == "humedad-suelo"){
              this.sensorHumedadSuelo = itemData.valor;
            }
            else if(doc.id == "temperatura-ambiente"){
              this.sensorTemperaturaAmbiente = itemData.valor;
            }
            else if(doc.id == "luz"){
              this.sensorLuz = itemData.valor;
              let luzFecha = itemData.fecha_update.toDate().toLocaleDateString()
              let luzHora = itemData.fecha_update.toDate().toLocaleTimeString()
              this.sensorLuzFecha = luzFecha+" "+luzHora;
            }
          });
        }, error => {
          console.error("Error al obtener la colección de sensores:", error);
        });

      } catch (error) {
        console.error("Error en fetchData:", error);
      }
    }
  },
  created() {
    this.fetchData();
  },
  mounted() {

  },
  beforeUnmount() {
    if (this.unsubscribeDocument) {
      this.unsubscribeDocument();
    }
    if (this.unsubscribeSensores) {
      this.unsubscribeSensores();
    }
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
