// import firebase from 'firebase/app';
// import 'firebase/firestore';

// const firebaseConfig = {
//   apiKey: "AIzaSyD0XCA5pL5swZE38N_XHT_JJT1Uc_OeIyg",
//   authDomain: 'fir-inv-72799.firebaseapp.com',
//   databaseURL: 'https://fir-inv-72799-default-rtdb.firebaseio.com',
//   projectId: 'fir-inv-72799',
//   storageBucket: 'fir-inv-72799.appspot.com',
//   messagingSenderId: '213323648848',
//   appId: '1:213323648848:web:5318a93dc667f0c10ba655',
// };

// const firebaseApp = firebase.initializeApp(firebaseConfig);
// const db = firebaseApp.firestore();

// export { db };

import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

// Configuración de Firebase
const firebaseConfig = {
  apiKey: "AIzaSyD0XCA5pL5swZE38N_XHT_JJT1Uc_OeIyg",
  authDomain: "fir-inv-72799.firebaseapp.com",
  databaseURL: "https://fir-inv-72799-default-rtdb.firebaseio.com",
  projectId: "fir-inv-72799",
  storageBucket: "fir-inv-72799.appspot.com",
  messagingSenderId: "213323648848",
  appId: "1:213323648848:web:5318a93dc667f0c10ba655",
};

// Inicializa Firebase
const firebaseApp = firebase.initializeApp(firebaseConfig);

// Servicios de Firebase
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();
const googleProvider = new firebase.auth.GoogleAuthProvider();

// Exporta los servicios
export { db, auth, googleProvider };
