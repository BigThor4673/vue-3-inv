import firebase from "../firebase";

// const db = firebase.collection("/inv-data/Inv-001/sensores");
const db = firebase.collection("/inv-data/Inv-001/maceteros");

class SensoresService {

  getAll() {
    return db;
  }
}

export default new SensoresService();
