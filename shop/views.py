from django.shortcuts import render
import random
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
from shop.models import ProductsModel


def home(request):
    obj_product = ProductsModel.objects.all()
    # random.shuffle(obj_product)
    paginator= Paginator(obj_product,10)
    try:
        page=int(request.GET.get('page','1'))
    except :
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'products':obj_product,'pg':pro})
def productDetail(req,slug):
    prod_obj=ProductsModel.objects.get(slug=slug)
    return render(req,'product_details.html',{'products':prod_obj})

