import { createRouter, createWebHistory } from "vue-router";
import Sensores from "../components/Sensores";
import Login from "../components/Login.vue";
import { auth } from "../firebase";
import { checkUserAccess } from "../services/authService";

const routes = [
    { 
        path: "/login", 
        name: "Login", 
        component: Login 
    },
    {
        path: "/",
        alias: "/planta",
        name: "planta",
        component: Sensores,
        meta: { requiresAuth: true }, // Ruta protegida
    }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Middleware para proteger rutas
router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth) {
    const user = auth.currentUser;

    if (!user) {
      next("/login");
    } else {
      const hasAccess = await checkUserAccess(user.email);
      if (hasAccess) {
        next();
      } else {
        alert("No tienes permiso para acceder a esta página.");
        next("/login");
      }
    }
  } else {
    next();
  }
});

export default router;
