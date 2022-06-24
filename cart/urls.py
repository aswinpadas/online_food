from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cartView, name='cart'),
    path('addtocart/<int:prodect_id>/', views.addCart, name='addtocart')
]
