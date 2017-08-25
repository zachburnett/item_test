from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
   url(r'^add_item$', views.add_item),
   url(r'^add_proccess$', views.add_proccess),
   url(r'^logout$',views.logout),
   url(r'^remove/(?P<item>\d+)/(?P<user>\d+)$', views.remove),
   url(r'^add/(?P<item>\d+)/(?P<user>\d+)$', views.add),
   url(r'^delete/(?P<item>\d+)/(?P<user>\d+)$', views.delete),
   url(r'^showall/(?P<item>\d+)$', views.showall),
   url(r'^show/(?P<item>\d+)$',views.show),
   
]