from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /autologin/username/00000000-0000-0000-0000-000000000000
    url(r'^(?P<username>[-\w]+)/(?P<token>[-\w]+)/$', views.autologin, name='login'),
]