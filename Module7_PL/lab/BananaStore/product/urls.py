from django.conf.urls import url
from . import views

app_name = "product_ns"

urlpatterns = [
    url(r'^$', views.add_product, name="add_product"),
]
