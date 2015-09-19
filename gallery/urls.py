from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /gallery/
    url(r'^$', views.index, name='index'),
    # ex: /gallery/europe/
    url(r'^(?P<gallery_id>[-\w]+)/$', views.gallery, name='gallery'),
    # ex: /gallery/europe/5
    url(r'^(?P<gallery_id>[-\w]+)/(?P<image_id>[0-9]+)/$', views.image, name='image'),
    # ex: /gallery/europe/5/comment
    url(r'^(?P<gallery_id>[-\w]+)/(?P<image_id>[0-9]+)/comment/$', views.comment, name='comment'),
]