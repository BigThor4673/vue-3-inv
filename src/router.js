import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  // {
  //   path: "/",
  //   alias: "/tutorials",
  //   name: "tutorials",
  //   component: () => import("./components/TutorialsList")
  // },
  {
    path: "/",
    alias: "/planta",
    name: "planta",
    component: () => import("./components/Sensores")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddTutorial")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;