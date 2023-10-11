from django.utils import timezone
from django.db import models

# Create your models here.
class Cultivo(models.Model):
    nombre = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'cultivo'
        
    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
        
class Tiptrata(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    class Meta:
        managed = True
        db_table = 'tiptrata'
        
    def __str__(self) -> str:
        return self.nombre
        
        
class Tratamiento(models.Model):
    fecha_aplicacion = models.DateField()
    dosis = models.FloatField()
    resultado = models.CharField(max_length=250)
    tipo_tratamiento = models.ForeignKey(Tiptrata, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'tratamiento'
        
    def __str__(self) -> str:
        return self.resultado
    
    
class Tsensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'tsensor'
        
    def __str__(self) -> str:
        return self.nombre
    
    
class Sensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)
    tipo_sensor = models.ForeignKey(Tsensor, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sensor'
        
    def __str__(self) -> str:
        return self.nombre
        
        
        