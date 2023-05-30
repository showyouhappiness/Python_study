from django.urls import path
from . import views
from rest_framework import urlpatterns
from django.conf.urls import url

app_name = 'blogPost'  # 为了区分不同app下的同名模板文件

urlpatternsView = [
    url(r'^blogPostList/$', views.blogPostList, name='blogPostList'),
    url(r'^blogPostDetail/(?P<pk>[0-9]+)/$', views.blogPostDetail, name='blogPostDetail'),  # 正则表达式, 作用是匹配url中的数字
]

urlpatterns = urlpatterns.format_suffix_patterns(urlpatternsView)
