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
from home.views import index
from home import urls as urls_home
from products.views import all_products
from accounts import urls as urls_accounts
from cart import urls as cart_urls
from checkout import urls as checkout_url
from bugs import urls as urls_bugs
from features import urls as urls_features
from graphs import urls as urls_graphs
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^home/', include(urls_home)),
    url(r'^products/', all_products, name='all_products_link'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^shopping_cart/', include(cart_urls.urlpatterns)),
    url(r'^checkout/', include(checkout_url.urlpatterns),name='checkout_link'),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^features/', include(urls_features)),
    url(r'^graphs/', include(urls_graphs)),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)