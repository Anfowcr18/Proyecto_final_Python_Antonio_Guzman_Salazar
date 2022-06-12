from ast import Delete
from distutils.command.upload import upload
from django.db import models

class libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_lenght=100,verbose_name='Titulo')
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion=models.TextField(null=True)
    
    def __str__(self):
        fila="titulo: " + self.titulo + "-" + "descripcion: " +self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class usuario(models.Model):
    idus=models.AutoField(primary_key=True)
    nombre=models.CharField(max_lenght=100,verbose_name='nombre')
    
    def __str__(self):
        fila="nombre: " + self.nombre 
        return fila

class adquisicion(models.Model):
    ida=models.AutoField(primary_key=True)
    id=models.IntegerField(null=True)
    idus=models.IntegerField(null=True)

    def __str__(self):
        fila= "id: " +self.id + "-" + "idus: " +self.idus
        return fila




# Create your models here.
