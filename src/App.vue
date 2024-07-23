<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand"><img src="./assets/images/logo.png" alt="Logo" ><span>PLANTITA</span></router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/planta" class="nav-link">Planta 🪴</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/calendario" class="nav-link">Calendario 📅</router-link>
        </li>
      </div>
    </nav>

    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style scoped>
  body {
    margin: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #app {
    width: 100%;
    height: 100vh;
    background: linear-gradient(-7deg, transparent 50%, #9CE5CB 50%);
  }


    /* body {
      margin: 0;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      width: 100%;
      height: 100vh;
      max-height: 575px;
      background: linear-gradient(-7deg, transparent 50%, #9CE5CB 50%);
    }
    .circle {
      width: 100px;
      height: 100px;
      background-color: transparent;
      border: 4px solid rgba(255, 255, 255, 0.5);
      border-radius: 50%;
      position: absolute;
      top: 20%;
      left: 30%;
    }

    .square {
      width: 100px;
      height: 100px;
      background-color: transparent;
      border: 5px solid rgba(255, 255, 255, 0.5);
      position: absolute;
      top: 40%;
      left: 50%;
    }

    .triangle {
      width: 0;
      height: 0;
      border-left: 50px solid transparent;
      border-right: 50px solid transparent;
      border-bottom: 100px solid transparent;
      border-bottom-color: rgba(255, 255, 255, 0.5);
      position: absolute;
      top: 60%;
      left: 70%;
    } */

.navbar-brand img{
  width: 30px;
  height: 30px;
}

/* body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
} */

/* .container {
  width: 100%;
  height: 100vh;
  background: linear-gradient(-7deg, transparent 50%, #9CE5CB 50%);
} */

/* .container h2 {
  text-align: center;
  margin: 25px auto;
}
#app{
  background-image: url("./assets/vectors/fondo_1.svg");
  background-repeat: no-repeat, repeat;
  background-color: #0e5d1f;
} */
</style>