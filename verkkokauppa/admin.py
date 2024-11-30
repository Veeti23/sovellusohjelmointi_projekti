from django.contrib import admin
from .models import Product, Productdetail, Review

admin.site.register(Product)
admin.site.register(Productdetail)
admin.site.register(Review)