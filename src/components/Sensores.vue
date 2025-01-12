<template>
  <div class="card w-100 h-50 mx-auto mt-2 shadow" id="cardSensores">
    <div class="card-body">
      <!-- container info planta -->
      <div class="container">
        <header-planta :banco="plantaData.banco" :genetica="plantaData.tipo" :nombre="plantaData.nombre" />
      </div>
      <!-- container data y foto planta -->
      <div class="container">
        <div class="row" id="planta">
          <!-- widgets luz y edad -->
          <div class="col-sm-3 p-0">
            <div class="row">
              <div class="col-md-12 col-6">
                <!-- luz -->
                <indicador-widget :linea1="tiempo_luz" :linea2="sensorLuzFecha"
                  :linea3="!sensorLuz ? 'APAGADA' : 'ENCENDIDA'" :clase="!sensorLuz ? 'apagada' : 'encendida'" />
              </div>
              <div class="col-md-12 col-6">
                <!-- edad -->
                <indicador-widget :linea1="tiempo_edad_planta"
                  :linea2="plantaData.fecha_germinacion ? plantaData.fecha_germinacion.toDate().toLocaleDateString() : ''"
                  :linea3="'EDAD'" :clase="'edad'" />
              </div>
            </div>
          </div>
          <!-- imagen planta -->
          <div class="col-sm-6">
            <img src="../assets/images/weed.png" class="rounded mx-auto d-block img-responsive" alt="Planta">
          </div>
          <!-- widgets info -->
          <div class="col-sm-3 pl-0 pr-3">
            <div class="row">
              <div class="col-sm-12 col-4 px-1">
                <!-- humedad del suelo -->
                <sensor-widget :linea1="sensorHumedadSuelo + '%'" :linea2="'HUMEDAD DEL SUELO'"
                  :imagen="'humedad-suelo'" />
              </div>
              <div class="col-sm-12 col-4 px-1">
                <!-- temperatura ambiental -->
                <sensor-widget :linea1="sensorTemperaturaAmbiente + '°'" :linea2="'T° AMBIENTAL'"
                  :imagen="'temperatura-ambiente'" />
              </div>
              <div class="col-sm-12 col-4 px-1">
                <!-- humedad ambiental -->
                <sensor-widget :linea1="sensorHumedadAmbiente + '°'" :linea2="'HUMEDAD AMBIENTAL'"
                  :imagen="'humedad-ambiente'" />
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
  computed: {
    tiempo_luz() {
      if (!this.sensorLuzFecha) {
        return "-";
      }

      // Convertir el string a un formato de fecha compatible con JavaScript
      const [datePart, timePart] = this.sensorLuzFecha.split(' ');
      const [day, month, year] = datePart.split('/');
      const formattedDateStr = `${year}-${month}-${day}T${timePart}:00`;

      const sensorLuzFecha = new Date(formattedDateStr);
      const now = new Date();

      const diffMs = now - sensorLuzFecha;
      const diffHrs = Math.floor(diffMs / (1000 * 60 * 60));
      const diffMins = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));

      return `${diffHrs}h ${diffMins}min`;
    },
    tiempo_edad_planta() {
      const today = new Date();
      let date = this.plantaData.fecha_germinacion ? this.plantaData.fecha_germinacion.toDate() : today

      // Ajustar la hora en ambas fechas a medianoche para evitar errores en la zona horaria
      today.setHours(0, 0, 0, 0);
      date.setHours(0, 0, 0, 0);

      let months = (today.getFullYear() - date.getFullYear()) * 12 + (today.getMonth() - date.getMonth());
      let days = today.getDate() - date.getDate();

      // Si los días son negativos, reducir un mes y ajustar los días
      if (days < 0) {
        months -= 1;
        // Obtener el último día del mes anterior de "today"
        const previousMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        days += previousMonth.getDate();
      }

      return `${months}M y ${days}d`;
    }
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
            if (doc.id == "humedad-ambiente") {
              this.sensorHumedadAmbiente = itemData.valor;
            }
            else if (doc.id == "humedad-suelo") {
              this.sensorHumedadSuelo = itemData.valor;
            }
            else if (doc.id == "temperatura-ambiente") {
              this.sensorTemperaturaAmbiente = itemData.valor;
            }
            else if (doc.id == "luz") {
              console.log("======= LUZ ======== ");
              console.log("itemData: "+JSON.stringify(itemData));
              this.sensorLuz = itemData.valor;
              console.log("SensorLuz: " + this.sensorLuz);
              
              // let luzFecha = itemData.fecha_update ? itemData.fecha_update.toDate().toLocaleDateString() : null;
              // console.log("LuzFecha: " + luzFecha);
              // let luzHora = itemData.fecha_update ? itemData.fecha_update.toDate().toLocaleTimeString() : null;
              // console.log("LuzHora: " + luzHora);
              // this.sensorLuzFecha = luzFecha + " " + luzHora;
              this.sensorLuzFecha = itemData.fecha_string;
              console.log("SensorLuzFecha: " + this.sensorLuzFecha);

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

.widgetsLeft .linea2 {
  font-size: 0.85rem;
}

.widgetsLeft .linea3 {
  font-weight: 500;
  color: #877900;
}

.img-responsive {
  width: 50%; /* 50% de ancho en dispositivos móviles */
}

@media (min-width: 992px) { /* Punto de interrupción para pantallas grandes (computadoras) */
  .img-responsive {
    width: 75%; /* 75% de ancho en pantallas grandes */
  }
}

/* .widgetsLeft .linea3.encendida{
  color: rgb(255 255 0) !important;
}

.widgetsLeft .linea3.edad{
  color: rgb(68, 102, 227) !important;
} */
</style>
