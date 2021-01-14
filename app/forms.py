from django import forms
from .models import *

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField(max_value=2000, min_value=1)
    quantity = forms.IntegerField(max_value=20000, min_value=0)

class AttemptForm(forms.Form):
    coins_inserted = forms.CharField(max_length=300)
    product_selected = forms.ModelChoiceField(Product.objects.all())
