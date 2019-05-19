"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from products.views import all_products
from accounts import urls as urls_accounts
from cart.views import add_to_cart, view_cart,remove_from_cart,remove_all_from_cart
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^view_cart/$', view_cart),
    url(r'^add_to_cart/(?P<id>\d+)$', add_to_cart, name='add_to_cart_link'),
    url(r'^clear_cart/$', remove_all_from_cart, name='remove_all_from_cart_link'),
    url(r'^remove_from_cart/(?P<id>\d+)$', remove_from_cart, name='remove_from_cart_link')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)