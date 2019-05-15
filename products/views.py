from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import AddProduct
# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {"all_products": all_products})

def addproduct(request):
    if request.method == "POST":
        submitted_form = AddProduct(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(all_products)
        else:
            return(request,"add_product.html",{
                'form':submitted_form
            })
    else:
        toadd_form = AddProduct()
        return render(request,"add_product.html",{
            'form' : toadd_form
        })