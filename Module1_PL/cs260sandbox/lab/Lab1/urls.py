from django.conf.urls import url
from django.views.generic import TemplateView
from Lab1.cart import views as cart_views

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^cart/$', cart_views.cart),
]
