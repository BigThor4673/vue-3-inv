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
    font-family: "Roboto", sans-serif;
  }

  #app {
    width: 100%;
    height: 100vh;
    background: linear-gradient(-7deg, transparent 50%, #9CE5CB 50%);
  }

.navbar-brand img{
  width: 30px;
  height: 30px;
}

</style>