from django.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url('payment/', include('testproject.payment.urls', namespace="payment_ns")),
]
