from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'product_price', 'stock', 'available','category', 'product_image']
    list_editable = ['product_price', 'stock', 'available', 'product_image']
    prepopulated_fields = {'slug': ('product_name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(ProductsModel, ProductAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
