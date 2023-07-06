from django.db import models

# Create your models here.



    
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")
    

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Id del producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True)
    nombre= models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre del producto")
    descripcion= models.CharField(max_length=100, blank=False, null=False, default="sin descripción", verbose_name="descripcion")
    precio = models.IntegerField(blank=False, null=False, default=0, verbose_name="precio producto")
    descsus = models.IntegerField(blank=False, null=True, verbose_name="descuento suscriptor")
    descof = models.IntegerField(blank=False, null=True, verbose_name="descuento oferta")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    


    def __str__(self):
        return self.nombreProducto