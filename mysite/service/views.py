# Create your views here.
from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from . import models


# Create your views here.


def postUser(request):
    if request.method == 'POST':
        # 获取页面输入的内容
        Appid = request.POST.get('Appid')
        # 查询数据库并返回相应的数据
        data = models.resource.objects.filter(appid=Appid)
        return render(request, 'post.html', {'data': data})
    else:
        return render(request, 'post.html')


# 添加用户信息
def addUser(request):
    if request.method == 'GET':
        return render(request, 'add_info.html')
    try:
        # 获取页面输入的内容
        Appid = request.POST.get('Appid')
        Service_id = request.POST.get('Service_id')
        Service_name = request.POST.get('Service_name')
        Appid_service_max = request.POST.get('Appid_service_max')
        Appid_max = request.POST.get('Appid_max')
        Service_id_all = request.POST.get('Service_id_all')
        Appid_service_percent = request.POST.get('Appid_service_percent')
        Service_all_percent = request.POST.get('Service_all_percent')
        Service_total_cpu = request.POST.get('Service_total_cpu')
        Service_total_gpu = request.POST.get('Service_total_gpu')
        Service_total_num = request.POST.get('Service_total_num')
        Resource_type = request.POST.get('Resource_type')
        Need_cpu = request.POST.get('Need_cpu')
        Need_gpu = request.POST.get('Need_gpu')
        Need_num = request.POST.get('Need_num')
        Data_time = request.POST.get('Data_time')
        Amount = request.POST.get('Amount')
        model = request.POST.get('model')

        # 关联表添加数据
        models.asset_type.objects.create(service_id=Service_id, id=Appid, amount=Amount, model=model)

        # 查询数据库并添加相应的数据
        models.resource.objects.create(appid=Appid, service_id=Service_id, service_name=Service_name,
                                       appid_service_max=Appid_service_max, appid_max=Appid_max,
                                       service_id_all=Service_id_all, appid_service_percent=Appid_service_percent,
                                       service_all_percent=Service_all_percent, service_total_cpu=Service_total_cpu,
                                       service_total_gpu=Service_total_gpu, service_total_num=Service_total_num,
                                       resource_type=Resource_type, need_cpu=Need_cpu, need_gpu=Need_gpu,
                                       need_num=Need_num, data_time=Data_time)

        # 提交事务
        transaction.commit()
    except:
        # 如果出现任何异常，回滚事务
        transaction.rollback()
        # 抛出异常或者返回错误信息
        raise
    # 如果正常，重定向到详情页面
    return redirect('/service/service_detail/')


# 获取用户信息
def getUserInfo(request):
    if request.method == 'GET':
        # 查询数据库所有的数据且含有关联的数据
        data = models.resource.objects.all()
        return render(request, 'get.html', {'data': data})
    else:
        return render(request, 'get.html')


# 删除用户信息
def deleteUser(request):
    if request.method == 'GET':
        # 获取页面输入的内容
        Appid = request.GET.get('id')
        # 查询数据库并返回相应的数据
        models.resource.objects.filter(id=Appid).delete()
        # 重定向到get页面
        return redirect('/service/service_detail/')
