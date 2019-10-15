from django.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^menu/', include('BananaStore.menu.urls',namespace="menu_ns")),
]
