from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin

from testproject.payment import views as payment_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^payment/$', payment_views.pay),
]


