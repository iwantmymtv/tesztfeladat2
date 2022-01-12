from django.views.generic import ListView,DetailView

from .models import Product,Category

class CategoryListView(ListView):

    model = Category
    paginate_by = 6  
    template_name = "products/categories.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryDetailView(DetailView):

    model = Category
    template_name = "products/category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductListView(ListView):

    model = Product
    paginate_by = 6  
    template_name = "products/products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductDetailView(DetailView):

    model = Product
    template_name = "products/details.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context