from django.conf.urls import patterns, url
from stores import views

urlpatterns = patterns('',
                    
    url(r'^info/$', views.StoreInfo.as_view()),
    )