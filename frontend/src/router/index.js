import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import TournamentsView from "@/views/TournamentsView.vue";
import LoginView from "@/views/LoginView.vue";
import TournamentDetailsView from "@/views/TournamentDetailsView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/tournaments",
      name: "tournaments",
      component: TournamentsView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/tournaments/:tournamentId",
      name: "tournamentDetails",
      component: TournamentDetailsView,
    },
  ],
});

export default router;