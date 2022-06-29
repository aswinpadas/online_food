from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.models import *

from django.core.exceptions import ObjectDoesNotExist


def cartView(req):
    ct_obj = CartItemModel.objects.all().filter(cart__cart_id=c_id(req))
    return render(req, 'cart.html', {'cart': ct_obj})


def c_id(req):
    ct_id = req.session.session_key
    if not ct_id:
        req.session.create()
        return req.session.session_key
    return ct_id


def addCart(req, prodect_id):
    try:
        cart = CartModel.objects.get(cart_id=c_id(req))
    except CartModel.DoesNotExist:
        cart = CartModel.objects.create(cart_id=c_id(req))
        cart.save()

    product = ProductsModel.objects.get(id=prodect_id)
    try:
        ct_items = CartItemModel.objects.get(prod=product, cart=cart)
        if ct_items.qty < ct_items.prod.stock:
            ct_items.qty += 1
    except CartItemModel.DoesNotExist:
        ct_items = CartItemModel.objects.create(prod=product, cart=cart, qty=1)
    ct_items.save()
    # return HttpResponse('ADDED TO CART <a href="/">return</a>')
    return redirect('cart')


def minCart(req,prod):
    ct_obj= CartItemModel.objects.get(prod__slug=prod)
    if ct_obj.qty > 1:
        ct_obj.qty-=1
    ct_obj.save()
    return redirect('cart')
def deleteCart(req,prod):
    ct_obj = CartItemModel.objects.get(prod__slug=prod)
    ct_obj.delete()
    return redirect('cart')
