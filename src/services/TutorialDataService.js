import firebase from "../firebase";

const db = firebase.collection("/tutorials");
const dbHumedadTierra = firebase.collection("/inv-data/Inv-001/sensores/humedad-tierra/valor");

class TutorialDataService {
  getHumedadTierra(){
    console.log("****** Service - getHumedadTierra:", dbHumedadTierra)
    return dbHumedadTierra;
  }

  getAll() {
    return db;
  }

  create(tutorial) {
    return db.add(tutorial);
  }

  update(id, value) {
    return db.doc(id).update(value);
  }

  delete(id) {
    return db.doc(id).delete();
  }
}

export default new TutorialDataService();
