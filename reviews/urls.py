from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^(?P<id>\d+)/$',views.review),
    url(r'^(?P<id>\d+)/addreview', views.review)
]