from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm, PaymentForm
from django.utils import timezone
from products.models import Product
from .models import Order, OrderLineItem
from django.core.mail import send_mail
from django.contrib import messages
import stripe
# Create your views here.
@login_required()
def checkout(request):
    if request.method == 'GET':
        cart = request.session.get('cart', {})
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'checkout.html', {
            'cart': cart,
            'order_form':order_form,
            'payment_form':payment_form,
            'stripe_publishable_key':settings.STRIPE_PUBLISHABLE_KEY
    })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # to process the post via POST
        cart = request.session.get('cart', {})
        total_cost = 0
        for cart_item in cart.values():
            total_cost += int(cart_item['qty']) * float(cart_item['product']['price'])
            floated_total_cost = float(total_cost)
        print(floated_total_cost) 
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST) 
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_token = request.POST.get('stripe_id')
            order.purchased_at = timezone.now()
            order.ordered_by = request.user
            order.save()
            
            for cart_item in cart.values():
                post_id = cart_item['product']['id']
                post = Product.objects.get(pk=post_id)
                order_line_item = OrderLineItem(
                    post = post,
                    order = order,
                    quantity = cart_item['qty']
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(floated_total_cost * 100),
                    currency = "sgd",
                    description = "Order ID #" + str(order.id),
                    source= order.stripe_token
                    )
            except stripe.error.CardError as e: 
                print (e)
                return HttpResponse("Card problem")
                
            if customer.paid:
                # request.session['cart'] = {}
                # subject = "Your invoice for your order " + str(order.id)
                # message = "Your order has been processed and will be shipped to you shortly"
                # email_from = settings.EMAIL_HOST_USER
             
                # send_to = ['chanhelmy@gmail.com']
                # send_mail(subject, message, email_from, send_to)
                # return  HttpResponse("Payment successful")
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('all_products_link'))
            else:
                messages.error(request, "Unable to take payment")
                # return HttpResponse("Payment failed")
            
        else:
            print(order_form.is_valid())
            print(payment_form.is_valid())
            print(payment_form.errors)
        
