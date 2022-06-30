from django.contrib import admin
# Register your models here.
from .models import *


class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','cart_id','date_added']


class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['id','prod','cart','qty']


admin.site.register(CartModel,CartModelAdmin)
admin.site.register(CartItemModel,CartItemModelAdmin)
