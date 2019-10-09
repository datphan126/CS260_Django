from django.urls import path
from . import views

from testproject.payment import views as payment_views

app_name = "payment_ns"

urlpatterns = [
    path('', payment_views.pay, name="pay"),
    path('help/', payment_views.help, name="help"),
]

