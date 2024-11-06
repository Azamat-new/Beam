from django.contrib import admin
from .models import ProductImage, Product, Category, Order


admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
