from django import forms
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuarioPersonalizadoCreationForm(UserCreationForm):
    
    password2 = forms.CharField(
        label="Confirme sua senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
            'id':'password2',
            }
        )
        
       
    )
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nome', 'email','password1', 'password2']
      
class UsuarioPersonalizadoAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
