import datetime

from django.db import models
from django.utils import timezone  # 用于比较时间,时区相关的工具模块


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'Question'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, to_field='id', verbose_name='问题')
    choice_text = models.CharField(max_length=200, verbose_name='选项')
    votes = models.IntegerField(default=0, verbose_name='票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'Choice'
