from django.urls import path
from . import views

app_name = 'polls'  # 为了区分不同app下的同名模板文件
# urlpatterns = [
#     path(r'', views.index, name='index'),
#     path(r'<int:question_id>/', views.detail, name='detail'),
#     path(r'<int:question_id>/results/', views.results, name='results'),
#     path(r'<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'<int:pk>/', views.DetailView.as_view(), name='detail'),
    path(r'<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
]