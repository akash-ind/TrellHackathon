from trell import views
from django.urls import path

app_name="trell"

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path('register', views.register, name="register"),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('load_users', views.load_users),
    path('load_trails', views.load_trails),
    path('change_users', views.change_users),
]
