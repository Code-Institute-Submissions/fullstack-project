from django.shortcuts import render,get_object_or_404, redirect
from products.models import Product
from products.views import all_products
from .forms import AddToCartForm
# Create your views here.
def add_to_cart(request,id):
    post = get_object_or_404(Product, pk=id)
    # print("-------------------------")
    # print(post)
    cart = request.session.get('cart',{})
    add_to_cart_form = AddToCartForm(request.POST)
    qty = add_to_cart_form['qty']
    price = str(post.price)
    if id not in cart:
        cart[id]={
            'product':{
                'id':id,
                'name':post.name,
                'price':price,
            },
        'qty': int(qty.value())
        }
    else:
        cart[id]['qty'] = cart[id]['qty'] + int(qty.value())
    
    request.session['cart'] = cart
    
    return redirect(all_products)

def view_cart(request):
    cart = request.session.get('cart',{})
    # print(cart)
    return render(request,'view_cart.html',{
        'cart':cart
    })

def remove_from_cart(request,id):
    cart = request.session.get('cart',{})
    del cart[id]
    request.session['cart'] = cart
    return redirect(view_cart)

def remove_all_from_cart(request):
    request.session['cart'] = {}
    return redirect(all_products)