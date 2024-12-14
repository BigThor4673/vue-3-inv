<template>
    <div>
      <h1>Iniciar sesión</h1>
      <button @click="handleLogin">Iniciar sesión con Google</button>
    </div>
  </template>
  
  <script>
  import { loginWithGoogle } from "../services/authService";
  
  export default {
    name: "Login",
    methods: {
      async handleLogin() {
        try {
          const user = await loginWithGoogle();
          console.log("Usuario autenticado:", user.email);
          this.$router.push("/planta"); // Redirige a la planta
        } catch (error) {
          console.error("Error durante el inicio de sesión:", error);
          alert("Error durante el inicio de sesión");
        }
      },
    },
  };
  </script>
  