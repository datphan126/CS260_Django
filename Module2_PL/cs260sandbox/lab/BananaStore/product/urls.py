from django.conf.urls import url
from . import views

app_name = "product_ns"

urlpatterns = [
    url(r'^$', views.pay, name="index"),
    url(r'^(?P<product>\D+)/', views.pay, name="details"),
]
