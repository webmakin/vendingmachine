from django.contrib import admin

from .models import Product, Purchase, Attempt

admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Attempt)
