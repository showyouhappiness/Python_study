from django.urls import path, re_path
from . import views  # 从自己的 app 目录引入 views

urlpatterns = [
    path('service_detail/', views.getUserInfo, name='serviceDetail'),
    path('post_detail/', views.postUser, name='postDetail'),
    path('delete_detail/', views.deleteUser, name='deleteDetail'),
    path('edit_detail/', views.editDetail, name='editDetail'),  # 通过url匹配获取id，不需要使用？来获取了
    path('add_detail/', views.addUser, name='addDetail'),
    path('edit_detail/<int:item_id>/', views.editDetail, name='edit_detail'),  # 通过url匹配获取id，不需要使用？来获取了
]
