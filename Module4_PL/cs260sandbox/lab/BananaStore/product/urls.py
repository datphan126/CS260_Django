from django.conf.urls import url
from . import views

app_name = "product_ns"

urlpatterns = [
    url(r'^$', views.product, name="index"),
    url(r'^(?P<product>\D+)/', views.product, name="details"),
]
