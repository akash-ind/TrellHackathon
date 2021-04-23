from trell import views
from django.urls import path

app_name="trell"

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path('register', views.register, name="register"),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('load_trails', views.populate_trails),
]
