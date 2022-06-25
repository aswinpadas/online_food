from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cartView, name='cart'),
    path('addtocart/<int:prodect_id>/', views.addCart, name='addtocart'),
    path('cart/delete/<str:prod>', views.deleteCart, name='delete'),
    path('cart/<str:prod>', views.minCart, name='min'),

]
