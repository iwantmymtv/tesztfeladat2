from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Cart,CartItem
from products.models import Product

def get_cart_id_from_session(request):
    return request.session.get('cart')

def store_cart_in_session(cart, session):
    session['cart'] = cart.pk
    session.save()
    return

def prepare_cart(cart, request):
    store_cart_in_session(cart, request.session)
    return cart

def get_anonymous_cart(request):
    cart_id = get_cart_id_from_session(request)
    try:
        cart = Cart.objects.get(pk=cart_id)
    except Cart.DoesNotExist:
        cart = None
    return cart

def get_cart(request, prepare=True):
    cart = get_anonymous_cart(request)
    if cart is None:
        cart = Cart.objects.create()
        cart.save()
    return prepare_cart(cart, request) if prepare else cart

def cart_view(request):
    cart = get_cart(request)
    ctx = {
        "cart":cart
    }
    return render(request,"cart/cart.html",ctx)

def add_to_cart(request,product_id:int):
    cart = get_cart(request)
    product = Product.objects.get(id = product_id)
    item,_ = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )
    print(item)
    if item.quantity +1 > product.in_stock:
        messages.error(request,"Cannot add to cart, only,{product.in_stock} product(s)  available.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    item.quantity += 1
    item.save
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
