from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductDetailView,
    ProductListView,
    )

app_name = "products"

urlpatterns = [
    path("",view=ProductListView.as_view(),name="product-list"),
    path("products/<slug:slug>", view=ProductDetailView.as_view(), name="product-detail"),
    path("categories/",view=CategoryListView.as_view(),name="category-list"),
    path("categories/<slug:slug>", view=CategoryDetailView.as_view(), name="category-detail"),
]