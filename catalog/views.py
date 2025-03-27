from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product, Contact


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }


class CatalogListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог'
    }


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'object_list': Contact.objects.all(),
        'title': 'Контакты'
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class BasketListView(ListView):
    model = Product
    extra_context = {
        'title': 'Корзина'
    }
    template_name = 'catalog/basket.html'
