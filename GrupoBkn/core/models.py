from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de producto")
    nombreProducto = models.CharField(max_length=80, blank=False, null=False, verbose_name="nombre del producto")
    precioProducto = models.IntegerField(blank=False, null=False, verbose_name="Precio del producto")
    descripcionProducto = models.CharField(max_length=200, blank= False, null=False, verbose_name="Descripción del producto")
    stockProducto = models.IntegerField(blank=False, null=False, verbose_name="Stock del Producto")
    imagenProducto = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen del Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombreProducto