from . import views
from django.urls import path

app_name = "usuarios"
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_usuario, name="login"),

]