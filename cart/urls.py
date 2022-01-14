from django.urls import path
from .views import cart_view,add_to_cart,delete_every_item

app_name="cart"

urlpatterns = [
    path('mine', cart_view, name='cart'),
    path('remove-all/', delete_every_item,name="remove-all"),
    path('add/<int:product_id>/<str:quantity>', add_to_cart, name='add-item'),
]