import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import TournamentsView from "@/views/TournamentsView.vue";
import LoginView from "@/views/LoginView.vue";
import TournamentDetailsView from "@/views/TournamentDetailsView.vue";
import ManageTournamentsView from "@/views/ManageTournamentsView.vue";
import AddTournamentView from "@/views/AddTournamentView.vue";
import EditTournamentView from "@/views/EditTournamentView.vue";

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
    {
      path: "/admin/tournaments",
      name: "manageTournaments",
      component: ManageTournamentsView,
    },
    {
      path: "/admin/tournaments/new",
      name: "addTournament",
      component: AddTournamentView,
    },
    {
      path: "/admin/tournaments/:tournamentId",
      name: "editTournament",
      component: EditTournamentView,
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: { name: "home" },
    }
  ],
});

export default router;