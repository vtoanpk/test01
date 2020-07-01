import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('lth', 'Sort by price : Low to High'),
        ('htl', 'Sort by price : High to Low'),
    )

    ordering = django_filters.ChoiceFilter(label='Sort by price: ', choices=CHOICES, method='filter_by_order')
    class Meta:
        model = Product
        fields = []

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value =='lth' else '-price'
        return queryset.order_by(expression)