from django.db import models


# Create your models here.
class blogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogPost'  # 指定数据表名
        app_label = 'blogPost'  # 指定该model属于哪个app
