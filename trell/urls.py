from trell import views
from django.urls import path

app_name="trell"

urlpatterns = [
    path("", views.login, name="login"),
    path('register', views.register, name="registed"),
]
