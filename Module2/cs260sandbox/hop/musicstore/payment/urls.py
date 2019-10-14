from django.conf.urls import url
from . import views

from musicstore.payment import views as payment_views

app_name = "payment_ns"

urlpatterns = [
    url(r'^$', payment_views.pay, name="pay"),
    url(r'^help/$', payment_views.help, name="help"),
    url(r'^(?P<payment_type>\D+)/',
        payment_views.pay, {'discount': '40'}),
]
