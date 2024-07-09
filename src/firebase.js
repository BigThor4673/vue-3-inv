import firebase from "firebase/app";
import "firebase/firestore";

// let config = {
//   apiKey: "xxx",
//   authDomain: "bezkoder-firebase.firebaseapp.com",
//   databaseURL: "https://bezkoder-firebase.firebaseio.com",
//   projectId: "bezkoder-firebase",
//   storageBucket: "bezkoder-firebase.appspot.com",
//   messagingSenderId: "xxx",
//   appId: "xxx",
// };
let config = {
  apiKey: "AIzaSyD0XCA5pL5swZE38N_XHT_JJT1Uc_OeIyg",
  authDomain: 'fir-inv-72799.firebaseapp.com',
  databaseURL: 'https://fir-inv-72799-default-rtdb.firebaseio.com',
  projectId: 'fir-inv-72799',
  storageBucket: 'fir-inv-72799.appspot.com',
  messagingSenderId: '213323648848',
  appId: '1:213323648848:web:5318a93dc667f0c10ba655',
};

firebase.initializeApp(config);

export default firebase.firestore();
