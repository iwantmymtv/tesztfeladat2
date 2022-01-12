from django.db import models

class DateAwareModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        )

    class Meta:
        abstract = True

class Category(DateAwareModel,models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

class Product(DateAwareModel,models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/thumbnails")
    category = models.ForeignKey(
        'Category',
        related_name="products",
        on_delete=models.SET_NULL,
        null=True
        )
    in_stock = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
