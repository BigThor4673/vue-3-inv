<template>
  <div class="card w-100 h-50 mx-auto mt-2 shadow" id="cardSensores">
    <div class="card-body">
      <!-- container info planta -->
      <div class="container">
        <!-- Fila banco y genetica -->
        <div class="row">
          <!-- banco -->
          <div class="col-sm-6">
            <h6 class="float-left">Medical Seeds</h6>
          </div>
          <!-- genetica -->
          <div class="col-sm-6">
            <span class="badge badge-light float-right mr-4">INDICA</span>
          </div>
          <!-- nombre -->
          <div class="col-sm-12">
            <h3>Black Devil</h3>
          </div>
        </div>
      </div>
      <!-- container data y foto planta -->
      <div class="container">
        <div class="row" id="planta">
          <!-- widgets luz y edad -->
          <div class="col-sm-3 p-0">
            <!-- luz -->
            <div class="row widgetsLeft ml-4 mb-4 pb-4 pt-4">
              <div class="col-sm-12 p-0">
                <p class="linea1 m-0"><strong>18.5 Hr</strong></p>
              </div>
              <div class="col-sm-12 p-0">
                <p class="linea2 m-0">08/05/2024 04:20</p>
              </div>
              <div class="col-sm-12 p-0">
                <p class="linea3 m-0 encendida">ENCENDIDA</p>
              </div>
            </div>
            <!-- edad -->
            <div class="row widgetsLeft ml-4 mb-4 pb-4 pt-4">
              <div class="col-sm-12 p-0">
                <p class="linea1 m-0"><strong>1M y 2D</strong></p>
              </div>
              <div class="col-sm-12 p-0">
                <p class="linea2 m-0">06/04/2024</p>
              </div>
              <div class="col-sm-12 p-0">
                <p class="linea3 m-0 edad">EDAD</p>
              </div>
            </div>
          </div>
          <!-- imagen planta -->
          <div class="col-sm-6">
            <img src="../assets/images/weed.png" class="rounded mx-auto d-block w-75" alt="Planta">
          </div>
          <!-- widgets info -->
          <div class="col-sm-3 p-0">
            <!-- humedad del suelo -->
            <div class="row widgetsRight">
              <div class="col-sm-4">
                <img src="../assets/vectors/humedad_suelo.svg" class="rounded mx-auto d-block w-100 imgWidget" alt="humedad suelo">
              </div>
              <div class="col-sm-8">
                <p class="linea1"><strong>20%</strong></p>
                <p class="linea2"><span>HUMEDAD DEL SUELO</span></p>
              </div>
            </div>
            <!-- temperatura ambiental -->
            <div class="row widgetsRight">
              <div class="col-sm-4">
                <img src="../assets/vectors/humedad_suelo.svg" class="rounded mx-auto d-block w-100 imgWidget" alt="humedad suelo">
              </div>
              <div class="col-sm-8">
                <p class="linea1"><strong>31°</strong></p>
                <p class="linea2"><span>TEMPERATURA AMBIENTAL</span></p>
              </div>
            </div>
            <!-- humedad ambiental -->
            <div class="row widgetsRight">
              <div class="col-sm-4">
                <img src="../assets/vectors/humedad_suelo.svg" class="rounded mx-auto d-block w-100 imgWidget" alt="humedad suelo">
              </div>
              <div class="col-sm-8">
                <p class="linea1"><strong>45°</strong></p>
                <p class="linea2"><span>HUMEDAD AMBIENTAL</span></p>
              </div>
            </div>
          </div>
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

.widgetsLeft .linea3.encendida{
  color: rgb(255 255 0) !important;
}

.widgetsLeft .linea3.edad{
  color: rgb(68, 102, 227) !important;
}
</style>
