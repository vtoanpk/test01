from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import ProductForm
from .models import Product
from .filters import ProductFilter
from users.decorators import unauthenticated_user
@unauthenticated_user
def index(request):
    return render(request, 'index.html')

@login_required
def product_list(request):
    count = Product.objects.count()
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'products/product_list.html', {'filter': product_filter, 'count': count})   

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('product_create')
    fields = ['name', 'description', 'price', 'image']

    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_edit.html'
    success_url = reverse_lazy('products')
    fields = ['name', 'description', 'price', 'image']


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    fields = ['name',]
    success_url = reverse_lazy('products')

class ProductSearchResultsView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/product_search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)|
            Q(price__icontains=query)
        )

