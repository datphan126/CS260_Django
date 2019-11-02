from django.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^menu/', include('BananaStore.product.urls',namespace="product_ns")),
]

