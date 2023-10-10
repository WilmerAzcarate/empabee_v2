from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .views import AuthUserManager
from django.db import models
from django.utils import timezone

# Create your models here.
class Genero(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    
class Pais(models.Model):
    code = models.SmallIntegerField()
    iso3166a1 = models.CharField(max_length=2)
    iso3166a2 = models.CharField(max_length=6)
    nombre = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'pais'

    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class Departamento(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.IntegerField()
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamento'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=535)
    codigo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ciudad'

    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class TIdentificacion(models.Model):
    nombre = models.CharField(max_length=45)
    diminutivo = models.CharField(max_length=3,null=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 't_identificacion'

    def __str__(self):
        return self.nombre+" ("+self.diminutivo+")"
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
class Persona(AbstractBaseUser,PermissionsMixin):
    p_nombre = models.CharField(max_length=45)
    s_nombre = models.CharField(max_length=45, blank=True, null=True)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=9,choices=Genero.choices)
    telefono = models.CharField(max_length=120)
    correo = models.CharField(max_length=120,null=True)
    n_identificacion = models.IntegerField(unique=True)
    ciudad_residencia = models.ForeignKey(Ciudad, models.DO_NOTHING,null=True,related_name='persona_residencia')
    ciudad_nacimiento = models.ForeignKey(Ciudad, models.DO_NOTHING,null=True,related_name='persona_nacimiento')
    t_identificacion = models.ForeignKey(TIdentificacion,models.DO_NOTHING,null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['p_nombre','p_apellido','n_identificacion']
    
    class Meta:
        managed = True
        db_table = 'persona'

    def __str__(self) -> str:
        p_nombre = self.p_nombre
        p_apellido = self.p_apellido
        return p_nombre+" "+p_apellido
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)