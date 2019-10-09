from django.urls import path
from . import views

from testproject.payment import views as payment_views

urlpatterns = [
    path('', payment_views.pay),
    path('help/', payment_views.help),
]

