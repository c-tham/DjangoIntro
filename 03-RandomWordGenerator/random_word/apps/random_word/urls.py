from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^rand$', views.rand), ### add this line
    url(r'^reset$', views.reset), ### add this line
]
