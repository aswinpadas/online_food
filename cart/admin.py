from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(CartModel)
admin.site.register(CartItemModel)
