from django.urls import path
from . import views

app_name = 'user'  # 为了区分不同app下的同名模板文件

urlpatterns = [
    # 用户管理
    path('user/list/', views.user_list, name="user_list"),
    path('user/add/', views.user_add, name="user_add"),
]

