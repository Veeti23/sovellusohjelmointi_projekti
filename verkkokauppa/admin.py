from django.contrib import admin

from .models import Product, Reviews, ProductDescription

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(ProductDescription)