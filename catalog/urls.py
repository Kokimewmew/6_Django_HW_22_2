from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, ContactsView, ProductsListview, ProductsDetailview

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductsListview.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductsDetailview.as_view(), name='products_detail')
]
