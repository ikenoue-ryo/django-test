from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^detail/(?P<pk>[0-9])/$',
        views.PostDetail.as_view(), name='post_detail'),
    url(r'^update/(?P<pk>[0-9])/$',
        views.PostUpdate.as_view(), name='post_update'),
    url(r'^delete/(?P<pk>[0-9])/$',
        views.PostDelete.as_view(), name='post_delete'),
]
