from django.shortcuts import render


# Create your views here.
from shop.models import ProductsModel


def home(request):
    obj_product = ProductsModel.objects.all()
    return render(request, 'index.html',{'products':obj_product})
def productDetail(req,slug):
    prod_obj=ProductsModel.objects.get(slug=slug)
    return render(req,'product_details.html',{'products':prod_obj})

