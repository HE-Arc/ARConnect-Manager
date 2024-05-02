from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register(r'tournaments', views.TournamentItemViewSet, basename='tournamentitem')

urlpatterns = [
    path("", include(router.urls)),


    #User registration, login, logout and details    
    path("user/register/", RegisterView.as_view(), name="register"),   #POST
    path("user/login/", LoginView.as_view(), name="login"),            #POST
    path("user/logout/", LogoutView.as_view(), name="logout"),         #POST
    path('user/', views.UserView.as_view(), name='user_details'),      #GET
]