from django.urls import path

from m2.stores import views as stores_views

urlpatterns = [
    path('', stores_views.details),
]
