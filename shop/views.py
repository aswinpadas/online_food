from django.shortcuts import render
import random
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
from cart.models import CartItemModel
from cart.views import c_id
from shop.models import ProductsModel


def home(request):
    obj_product = ProductsModel.objects.all()
    # random.shuffle(obj_product)
    paginator = Paginator(obj_product, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    ct_obj = CartItemModel.objects.all().filter(cart__cart_id=c_id(request))

    # print(str(obj_product),'\n***************************\n',str(ct_obj))
    return render(request, 'card.html', {'products': obj_product, 'pg': pro,'cart': ct_obj})

def homeFilter(request,filt):
    obj_product = ProductsModel.objects.filter(category__slug=filt)
    # random.shuffle(obj_product)
    paginator = Paginator(obj_product, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'products': obj_product, 'pg': pro})

def productDetail(req, slug):
    prod_obj = ProductsModel.objects.get(slug=slug)
    return render(req, 'product_details.html', {'products': prod_obj})
