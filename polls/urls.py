from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("cadastro", views.cadastro, name="cadastro"),
     path("mathquest", views.mathquest, name="mathquest"),
     path("matematica1ef", views.matematica1ef, name="matematica1ef"),
]

