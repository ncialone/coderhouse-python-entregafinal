from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import NewItemForm

def detalle(request, pk):
    #se pasa por parametro el id del item a buscar
    item = get_object_or_404(Item, pk=pk)
    #traemos 3 items relacionados de la misma categoria, filtrado por "no vendidos"
    items_relacionados = Item.objects.filter(categoria=item.categoria, vendido=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detalle.html',{
        'item': item,
        'items_relacionados': items_relacionados
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.creador = request.user
            item.save()
            
            return redirect('item:detalle', pk=item.id)
    form = NewItemForm()
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Nuevo item'
    })