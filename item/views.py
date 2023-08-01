from django.shortcuts import render, get_object_or_404
from .models import Item

def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_available=True)

    return render(request , 'detail.html',{
        'item' : item
    })
