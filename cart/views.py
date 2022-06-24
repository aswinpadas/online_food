from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.models import *

from django.core.exceptions import ObjectDoesNotExist


def cartView(req):
    ct_obj = CartItemModel.objects.all()
    return render(req, 'cart.html', {'cart': ct_obj})


def c_id(req):
    ct_id = req.session.session_key
    if not ct_id:
        ct_id = req.session.create
    return ct_id


def addCart(req, prodect_id):
    prodt = ProductsModel.objects.get(id=prodect_id)
    try:
        ct = CartModel.objects.get(cart_id=c_id(req))
    except CartModel.DoesNotExist:
        ct = CartModel.objects.create(cart_id=c_id(req))
        ct.save()
    try:
        ct_items = CartItemModel.objects.get(prod=prodt, cart=ct)
        if ct_items.qty < ct_items.prod.stock:
            ct_items.qty += 1
        ct_items.save()
    except CartItemModel.DoesNotExist:
        ct_items = CartItemModel.objects.create(prod=prodt, cart=ct, qty=1)
        ct_items.save()
    # return HttpResponse('ADDED TO CART <a href="/">return</a>')
    return redirect('cart')


def minCart(req):
    pass


def deleteCart(req):
    pass
