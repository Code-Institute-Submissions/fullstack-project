from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from cart.forms import AddToCartForm
# Create your views here.
def all_products(request):
    add_to_cart_form = AddToCartForm
    all_products = Product.objects.all()
    return render(request, "products.html", {"all_products": all_products,'form':add_to_cart_form})

