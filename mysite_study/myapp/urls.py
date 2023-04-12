from django.urls import path
from . import views

app_name = 'myapp'  # 为了区分不同app下的同名模板文件

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
]