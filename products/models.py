from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/thumbnails")
    category = models.ForeignKey(
        'Category',
        related_name="products",
        on_delete=SET_NULL,
        null=True
        )
    in_stock = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

