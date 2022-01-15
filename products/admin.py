from django.contrib import admin
from .models import Product,Category,RecommendedProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category","price","in_stock"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(RecommendedProduct)
class RecommendedProductAdmin(admin.ModelAdmin):
    pass