from django.conf.urls import url
from . import views

app_name = "product_ns"

urlpatterns = [
    url(r'^$', views.add_product, name="add_product"),
    url(r'^editproduct$', views.edit_product, name="edit_product"),
    url(r'^delete_product$', views.delete_product, name="delete_product"),
]
