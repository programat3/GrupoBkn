from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm

# Create your views here.

def index(request): 
    return render(request, 'core/index.html')

def administracion(request): 
    return render(request, 'core/administracion.html')

def bodega(request): 
    return render(request, 'core/bodega.html')

def boleta(request): 
    return render(request, 'core/boleta.html')

def carrito(request): 
    return render(request, 'core/carrito.html')

def ficha(request): 
    return render(request, 'core/ficha.html')

def historial_ventas(request): 
    return render(request, 'core/historial_ventas.html')

def ingresar(request): 
    return render(request, 'core/ingresar.html')

def menu(request): 
    return render(request, 'core/menu.html')

def mis_compras(request): 
    return render(request, 'core/mis_compras.html')

def misdatos(request): 
    return render(request, 'core/misdatos.html')

def nosotros(request): 
    return render(request, 'core/nosotros.html')

def registro(request): 
    return render(request, 'core/registro.html')

def ropa(request): 
    return render(request, 'core/ropa.html')

def usuarios(request): 
    return render(request, 'core/usuarios.html')

def productos(request):
    return render(request, "core/productos.html")


def producto_ficha(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}


    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos productos con el mismo id!"


    elif action == 'upd':
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)


    elif action == 'del':
        try:
            Producto.objects.get(id=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(productos, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"


    data["list"] = Producto.objects.all().order_by('id')
    return render(request, "core/productos.html", data)

def mantenedor_prod(request):
    Producto.objects.all().delete()
    Producto.objects.create(id=10, categoria=Categoria.objects.get(idCategoria=2), nombre="pedigree", descripcion='comida uwu', precio=7000, descsus=0, descof=2, imagen="images/PlaceHolder.png")
    Producto.objects.create(id=11, categoria=Categoria.objects.get(idCategoria=2), nombre="pedigree", descripcion='comida uwu', precio=7000, descsus=0, descof=2, imagen="images/PlaceHolder.png")
    Producto.objects.create(id=12, categoria=Categoria.objects.get(idCategoria=1), nombre="royal canin", descripcion='comida uwu', precio=8000, descsus=1, descof=2, imagen="images/PlaceHolder.png")
    Producto.objects.create(id=13, categoria=Categoria.objects.get(idCategoria=1), nombre="royal canin", descripcion='comida uwu', precio=8000, descsus=0, descof=2, imagen="images/PlaceHolder.png")
    Producto.objects.create(id=14, categoria=Categoria.objects.get(idCategoria=2), nombre="pedigree", descripcion='comida uwu', precio=7000, descsus=0, descof=2, imagen="images/PlaceHolder.png")
    Producto.objects.create(id=15, categoria=Categoria.objects.get(idCategoria=2), nombre="pedigree", descripcion='comida uwu', precio=7000, descsus=0, descof=2, imagen="images/PlaceHolder.png")
    return redirect(producto_ficha, action='ins', id = '-1')
