from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),

    path("login", views.login, name="login"),

    path("cadastro", views.cadastro, name="cadastro"),

    path("mathquest", views.mathquest, name="mathquest"),

    path("perfil", views.perfil, name="perfil"),

    path("sobre", views.sobre, name="sobre"),
     
    path("matematicaef1", views.matematicaef1, name="matematicaef1"),

    path("matematicaef2", views.matematicaef2, name="matematicaef2"),
    
    path("matematicaef3", views.matematicaef3, name="matematicaef3"),

    path("matematicaef4", views.matematicaef4, name="matematicaef4"),

    path("matematicaef5", views.matematicaef5, name="matematicaef5"),

    path("matematicaef6", views.matematicaef6, name="matematicaef6"),

    path("matematicaef7", views.matematicaef7, name="matematicaef7"),

    path("matematicaef8", views.matematicaef8, name="matematicaef8"),

    path("matematicaef9", views.matematicaef9, name="matematicaef9"),
    
]

