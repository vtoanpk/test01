from django.contrib import admin
from .models import Product

@admin.register(Product)
class PostAdmmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}