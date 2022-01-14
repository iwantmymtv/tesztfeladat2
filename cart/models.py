from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0,max_digits=12, decimal_places=2 )

    def __str__(self) -> str:
        return f"Guest, Items in cart: {self.items.all().count()} - total price: {self.get_total_price()} Ft" 

    def flush(self) -> None:
        self.items.all().delete()

    def get_total_price(self) -> int:
        total = 0
        for i in self.items.all():
            total += i.total_price()
        return total    
    
    def get_items_quantity(self) -> int:
        total = 0
        for i in self.items.all():
            total += i.quantity
        return total    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product= models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.product} x {self.quantity} - {self.total_price()}"
    
    def total_price(self) -> int:
        return self.quantity * self.product.price

    def remove_item(self) -> str:
        kwargs = {
            "product_id": self.product.id,
            "quantity":-1
        }
        return reverse("cart:add-item", kwargs=kwargs)

    def add_item(self) -> str:
        kwargs = {
            "product_id": self.product.id,
            "quantity":1
        }
        return reverse("cart:add-item", kwargs=kwargs)

    def remove_all_item(self) -> str:
        kwargs = {
            "product_id": self.product.id,
            "quantity":-self.quantity
        }
        return reverse("cart:add-item", kwargs=kwargs)

    #total_price = property(total_price)