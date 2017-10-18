from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    # url(r'^graph/$', views.graph.as_view(), name='graph'),
    url(r'^graph/$', views.graph, name='graph'),

]