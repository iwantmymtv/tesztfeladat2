from .views import get_cart

def cart_count(request):
    ctx= {
        'cart_count':get_cart(request).get_items_quantity(),
    }
    return ctx