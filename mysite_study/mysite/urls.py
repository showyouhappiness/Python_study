"""
Django 项目的 URL 声明，就像网站的“目录”。

mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
函数 include() 允许引用其它 URLconfs。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # 包含 polls 应用的 URL, 也就是 polls.urls。
    path('user/', include('user.urls')),  # 包含 user 应用的 URL, 也就是 user.urls。
    path('myapp/', include('myapp.urls')),  # 包含 myapp 应用的 URL, 也就是 myapp.urls。
    path('blogPost/', include('blogPost.urls')),  # 包含 blogPost 应用的 URL, 也就是 blogPost.urls。
]
