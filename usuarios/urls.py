from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "usuarios"
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_usuario, name="login"),
    path('sair/', views.sair, name="sair"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
