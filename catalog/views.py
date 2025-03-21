import json

from django.shortcuts import render

from catalog.models import Product, Contact


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)  # решил пока собранные данные выводить в консоль
    context = {
        'object_list': Contact.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': 'Товар'
    }
    return render(request, 'catalog/product.html', context)


def basket(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'catalog/basket.html', context)
