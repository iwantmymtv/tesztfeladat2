from django.urls import path
from .views import cart_view,add_to_cart

app_name="cart"

urlpatterns = [
    path('mine', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add-item'),
    #path('remove-single/<id>', views.remove_single_item,name="remove-single"),
    #path('remove-all/<id>', views.remove_all_item,name="remove-all"),
    #path('add-single/<id>', views.add_single_item,name="add-single"),
]