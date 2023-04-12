from django.shortcuts import render, HttpResponse, redirect
from django import forms
from .models import UserInfo


# Create your views here.
class UserModelForm(forms.ModelForm):
    # 验证规则
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "create_time", "gender", "depart"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 给所有字段的input框加上class:"form-control"
        for name, field in self.fields.items():
            if name == "password":
                continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_model_form_add(request):
    # 添加用户（ModelForm方式）
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})
    # 用户POST提交数据，数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()  # 自动存储到数据库中
        return redirect("/user/list")
    else:
        # 校验失败,form中包含错误信息和用户之前提交的数据
        return render(request, 'user_model_form_add.html', {"form": form})


def user_list(request):
    pass


def user_add(request):
    pass
