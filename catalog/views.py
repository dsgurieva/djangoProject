from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    context ={
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', context)

def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'main/home.html', context)

