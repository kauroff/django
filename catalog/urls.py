from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, product, basket, IndexView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
    path('basket/', basket, name='basket'),
]
