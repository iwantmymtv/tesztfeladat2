from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

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

def add_to_cart(request,product_id:int,quantity:str):
    #only negative and ppositive integers are valid
    if quantity.lstrip("-").isdigit():
        quantity = int(quantity)
    else:
        messages.error(request,f"Invalid value")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    cart = get_cart(request)
    product = Product.objects.get(id = product_id)
    item,_ = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    #check if quantity is 
    if item.quantity + quantity > product.in_stock:
        messages.error(request,f"Cannot add to cart, only {product.in_stock} product(s)  available at the moment.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # if quantity is 0 or smaller remove item
    elif item.quantity + quantity <= 0:
        item.delete()
        messages.success(request,"Removed from cart!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    item.quantity += quantity
    item.save()

    if quantity > 0:
        messages.success(request,"Item was successfully added to cart")
    else:
        messages.success(request,"Item was removed from cart")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_every_item(request):
    cart = get_cart(request)
    cart.flush()
    messages.success(request,"everthing vanished :(")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))