from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.list import MultipleObjectMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Product,Category
from .forms import RecommendProductForm

class CategoryListView(ListView):

    model = Category
    paginate_by = 6
    template_name = "products/categories.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryDetailView(DetailView,MultipleObjectMixin):

    model = Category    
    paginate_by = 3
    template_name = "products/category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        products = self.get_object().products.all()
        context = super().get_context_data(object_list=products,**kwargs)

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


class RecommendProductView(View):
    form_class = RecommendProductForm
    template_name = "products/recommend.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST,request.FILES)
        print("hello",form.changed_data)
        if form.is_valid():
            print("goos")
            form.save()
            messages.success(request,f"Thank you for your recommendation!")
            return HttpResponseRedirect(reverse("products:product-list"))

        return render(request, self.template_name, {'form': form})

    