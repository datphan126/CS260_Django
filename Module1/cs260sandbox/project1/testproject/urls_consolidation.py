from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='homepage.html')),
    path('payment/', include('testproject.payment.urls')),
]
