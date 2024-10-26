<template>
  <div class="card w-100 h-50 mx-auto mt-2 shadow" id="cardSensores">
    <div class="card-body">
      <!-- container info planta -->
      <div class="container">
        <header-planta
          :banco="'Medical Seeds'"
          :genetica="'INDICA'"
          :nombre="'Black Devil'"
        />
      </div>
      <!-- container data y foto planta -->
      <div class="container">
        <div class="row" id="planta">
          <!-- widgets luz y edad -->
          <div class="col-sm-3 p-0">
            <!-- luz -->
            <indicador-widget
              :linea1="'18.5 Hr'"
              :linea2="'08/05/2024 04:20'"
              :linea3="'ENCENDIDA'"
              :clase="'encendida'"

            />
            <!-- edad -->
            <indicador-widget
              :linea1="'1M y 2D'"
              :linea2="'06/04/2024'"
              :linea3="'EDAD'"
              :clase="'edad'"

            />
          </div>
          <!-- imagen planta -->
          <div class="col-sm-6">
            <img src="../assets/images/weed.png" class="rounded mx-auto d-block w-75" alt="Planta">
          </div>
          <!-- widgets info -->
          <div class="col-sm-3 p-0">
            <!-- humedad del suelo -->
            <sensor-widget
              :linea1="'20%'"
              :linea2="'HUMEDAD DEL SUELO'"
              :imagen="'humedad'"
            />
            <!-- temperatura ambiental -->
            <sensor-widget
              :linea1="'69°'"
              :linea2="'TEMPERATURA AMBIENTAL'"
              :imagen="'ambiente'"
            />
            <!-- humedad ambiental -->
            <sensor-widget
              :linea1="'45°'"
              :linea2="'HUMEDAD AMBIENTAL'"
              :imagen="'humedad'"
            />
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { db } from "../firebase";
import sensorWidget from "./WidgetSensor";
import indicadorWidget from "./WidgetIndicador";
import headerPlanta from "./WidgetHeaderPlanta";

export default {
  name: "sensores",
  components: { sensorWidget, indicadorWidget, headerPlanta },
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

#cardSensores {
  padding-top: 30px;
  min-height: 80vh;
  background-color: rgba(0, 0, 0, 0.1);
}

.widgetsLeft .linea2{
  font-size: 0.85rem;
}

.widgetsLeft .linea3{
  font-weight: 500;
  color: #877900;
}

/* .widgetsLeft .linea3.encendida{
  color: rgb(255 255 0) !important;
}

.widgetsLeft .linea3.edad{
  color: rgb(68, 102, 227) !important;
} */
</style>
