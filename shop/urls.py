from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>',views.productDetail,name='prod_detail'),
    path('filter/<str:filt>/',views.homeFilter,name='homefilter'),
]