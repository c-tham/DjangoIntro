from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process), ### add this line
    url(r'^result$', views.result), ### add this line
    url(r'^reset$', views.reset), ### add this line
]
