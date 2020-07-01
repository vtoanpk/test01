from django import forms 
from .models import Product 
  
  
# creating a form 
class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product
        fields = [ 
            "name", 
            "description",
            "price",
            "image",
            ]

