from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from cart.forms import AddToCartForm
# Create your views here.
def all_products(request):
    add_to_cart_form = AddToCartForm
    if 'search_terms' in request.GET:
         search_terms = request.GET.get('search_terms')
         all_products=Product.objects.filter(name__contains=search_terms)
    else:
        all_products = Product.objects.all()
    return render(request, "products.html", {
                "all_products": all_products,
                'form':add_to_cart_form
        
})

