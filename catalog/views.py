from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView

from django.shortcuts import render

from catalog.models import Product, Contact


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Каталог'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


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


class ContactsListView(ListView):
    model = Contact


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Товар'
    }
    return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    model = Product


def basket(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'catalog/basket.html', context)
