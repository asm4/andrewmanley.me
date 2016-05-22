from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thanks/$', views.contact_thanks, name='contact_thanks'),
]
