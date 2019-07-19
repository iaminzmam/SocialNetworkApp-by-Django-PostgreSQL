
from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post_details'),
        url(r'^like/$', views.LikePost, name='like_post'),
        url(r'^addcomment/$', views.addComment, name='add_comment'),
        url(r'^delcomment/$', views.delComment, name='del_comment')
]
