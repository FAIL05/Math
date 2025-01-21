from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


# Create your models here.

class Usuario(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Voce não informou um email válido')
        email = self.normalize_email(email)   
        user = self.model(email=email, **extra_fields) 
        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField (max_length=100)
    email = models.EmailField (max_length=100, unique=True)
    # senha = models.CharField (max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = Usuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__ (self):
        return self.email
    class Meta:
        verbose_name="usuario"