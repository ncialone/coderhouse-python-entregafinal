from django.shortcuts import render
from item.models import Categoria, Item

def index(request):
    #traigo 6 items que estan disponibles "no vendidos" y las categorias disponibles
    items = Item.objects.filter(vendido=False)[0:6]
    categorias = Categoria.objects.all()
    #agregamos items y categorias al context para que pueda representarlos
    return render(request, 'core/index.html', {
        'categorias': categorias,
        'items':items,
    })

def contacto(request):
    return render(request, 'core/contacto.html')