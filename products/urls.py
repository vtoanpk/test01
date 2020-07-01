from django.urls import path

from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, \
                    ProductSearchResultsView, product_list
urlpatterns = [
    path('search/', ProductSearchResultsView.as_view(), name='product_search'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('', product_list, name='products')
]