from django.shortcuts import render
from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_available=True)[0:8]
    categories = Category.objects.all()
    return render(request , 'index.html', {
        'items':items,
        'categories':categories
    })
    
