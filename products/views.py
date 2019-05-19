from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import AddProduct
# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {"all_products": all_products})

