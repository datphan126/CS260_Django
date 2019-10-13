from django.conf.urls import url
from django.views.generic import TemplateView

from testproject.payment import views as payment_views

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^payment/$', payment_views.pay),
    url(r'^payment/help/$', payment_views.help),
]


