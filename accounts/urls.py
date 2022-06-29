from django.urls import path
from .import views

urlpatterns = [
    path('accounts/signin',views.signin,name='signin'),
]