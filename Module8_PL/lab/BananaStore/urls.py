from django.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin
from BananaStore.product import views as product_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', product_views.get_all_products),
    url(r'^product/', include('BananaStore.product.urls',namespace="product_ns")),
]

