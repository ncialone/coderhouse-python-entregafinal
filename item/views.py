from django.shortcuts import render, get_object_or_404
from .models import Item

def detalle(request, pk):
    #se pasa por parametro el id del item a buscar
    item = get_object_or_404(Item, pk=pk)
    #traemos 3 items relacionados de la misma categoria, filtrado por "no vendidos"
    items_relacionados = Item.objects.filter(categoria=item.categoria, vendido=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detalle.html',{
        'item': item,
        'items_relacionados': items_relacionados
    })