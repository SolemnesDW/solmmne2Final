from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.view_index, name='home'),
	url(r'^categoria/(?P<pk>[\w-]+)/$', views.categoria, name='categoria'),
    url(r'^producto/(?P<pk>[\w-]+)/$', views.detalle_producto, name='detalle_producto'),
]