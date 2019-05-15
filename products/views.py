from django.shortcuts import render
from .models import Product
# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {"all_products": all_products})