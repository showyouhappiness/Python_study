# Generated by Django 3.2.18 on 2023-04-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset_type',
            fields=[
                ('service_id', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'asset_type',
            },
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('appid_service_max', models.IntegerField()),
                ('appid_max', models.IntegerField()),
                ('service_id_all', models.IntegerField()),
                ('appid_service_percent', models.FloatField()),
                ('service_all_percent', models.FloatField()),
                ('service_total_cpu', models.IntegerField()),
                ('service_total_gpu', models.IntegerField()),
                ('service_total_num', models.IntegerField()),
                ('resource_type', models.CharField(max_length=100)),
                ('need_cpu', models.IntegerField()),
                ('need_gpu', models.IntegerField()),
                ('need_num', models.IntegerField()),
                ('data_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'resource',
            },
        ),
    ]
