from django.urls import path, re_path
from . import views  # 从自己的 app 目录引入 views

urlpatterns = [
    re_path(r'service_detail/', views.getUserInfo, name='serviceDetail'),
    re_path(r'post_detail/', views.postUser, name='postDetail'),
    re_path(r'delete_detail/', views.deleteUser, name='deleteDetail'),
    re_path(r'edit_detail/<int:id>/', views.editDetail, name='editDetail'),  # 通过url匹配获取id，不需要使用？来获取了
    re_path(r'add_detail/', views.addUser, name='addDetail'),
]
