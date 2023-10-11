from django.db import models
from general.models import *
from django.utils import timezone

# Create your models here.
class EspeciePez(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=2000,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'especie_pez'
    
    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Estanque(models.Model):
    nombre = models.CharField(max_length=45)
    feinicio = models.DateField()
    fefinal = models.DateField()
    especies = models.CharField(max_length=150)
    cantpeces = models.IntegerField()
    alimentacion = models.CharField(max_length=150)
    frecualimentacion = models.CharField(max_length=150)
    tiemcultivo = models.IntegerField()
    cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING)
    especie_pez = models.ForeignKey(EspeciePez, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'estanque'
        
    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
    
class ProduccionEstanque(models.Model):
    idproduccion_colmena = models.AutoField(primary_key=True)
    cant_peces = models.FloatField(blank=True, null=True)
    fecha = models.DateField()
    estanque = models.ForeignKey(Estanque, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'produccion_estanque'
    
    def __str__(self) -> str:
        return self.fecha+" "+self.estanque
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
        
class InfotrataEstanque(models.Model):
    nombre = models.TextField()
    f_inicio = models.DateField()
    f_fin = models.DateField()
    tratamiento = models.ForeignKey(Tratamiento, models.DO_NOTHING)
    estanque_id = models.ForeignKey(
        Estanque, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'infotrata_estanque'
        
    def __str__(self) -> str:
        return self.fecha
    
    
class MSensorEstanque(models.Model):
    fechahora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING)
    estanque = models.ForeignKey(Estanque, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'm_sensor_estanque'