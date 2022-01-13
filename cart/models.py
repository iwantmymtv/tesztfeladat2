from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0,max_digits=12, decimal_places=2 )

    def __str__(self):
        if self.user:
            return f"{self.user}, Items in cart: {self.items.all().count()}" 
        else:
            return f"Guest, Items in cart: {self.items.all().count()} - total price: {self.total}" 

    def flush(self):
        self.items.all().delete()

    def get_total_price(self):
        total = 0
        for i in self.items.all():
            total += i.total_price
        return total    
    
    def get_items_quantity(self):
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
    
    def __str__(self):
        return f"{self.product} x {self.quantity} - {self.total_price()}"
    
    def total_price(self):
        return self.quantity * self.product.price

    def remove_item(self):
        return reverse("cart:remove-item", kwargs={"id": self.id})

    def add_item(self):
        return reverse("cart:add-item", kwargs={"id": self.id})

    def remove_all_item(self):
        return reverse("cart:remove-all", kwargs={"id": self.id})

    #total_price = property(total_price)