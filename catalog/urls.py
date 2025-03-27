from django.urls import path

from blog.views import PostListView
from catalog.apps import CatalogConfig
from catalog.views import IndexView, CatalogListView, ProductDetailView, ContactsView, BasketListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('basket/', BasketListView.as_view(), name='basket'),
]
