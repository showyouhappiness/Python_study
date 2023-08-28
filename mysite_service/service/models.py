from django.db import models


class asset_type(models.Model):
    service_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    amount = models.IntegerField()
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'asset_type'


# Create your models here.
class resource(models.Model):
    appid = models.CharField(max_length=100)
    service = models.ForeignKey(asset_type, on_delete=models.CASCADE,
                                to_field='service_id')  # 外键,关联asset_type表,on_delete的值代表删除关联数据时,当前数据也删除
    service_name = models.CharField(max_length=100)
    appid_service_max = models.IntegerField()
    appid_max = models.IntegerField()
    service_id_all = models.IntegerField()
    appid_service_percent = models.FloatField()
    service_all_percent = models.FloatField()
    service_total_cpu = models.IntegerField()
    service_total_gpu = models.IntegerField()
    service_total_num = models.IntegerField()
    resource_type = models.CharField(max_length=100)
    need_cpu = models.IntegerField()
    need_gpu = models.IntegerField()
    need_num = models.IntegerField()
    data_time = models.DateTimeField()

    class Meta:
        db_table = 'resource'
