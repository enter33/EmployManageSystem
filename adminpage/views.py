from django.shortcuts import render, redirect
from django import forms
from adminpage import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from utils.md5 import md5
# Create your views here.


class AdminModelForm(forms.ModelForm):
    '''
    管理员账户数据库的ModelForm
    '''
    # 新加一个确认密码字段，但是不保存在数据库中，widget是插件，表示是密码样式，且不置空
    confirm_password = forms.CharField(widget=forms.PasswordInput(render_value=True), label='确认密码')

    class Meta:
        model = models.Admin
        fields = '__all__'
        # 对于想更改插件的字段，如下写
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    # 钩子方法，在提交数据，判断合法性前自动调用，判断密码与确认密码是否一致
    def clean_confirm_password(self):
        '''
        校验密码与确认密码是否一致
        :return:
        '''
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        confirm_password = md5(confirm_password)
        if password != confirm_password:
            raise ValidationError('密码不一致')

        return confirm_password

    def clean_password(self):
        '''
        加密密码
        :return:
        '''
        password = self.cleaned_data.get('password')
        return md5(password)


class AdminEditModelForm(forms.ModelForm):
    '''
    编辑页面ModelForm
    '''
    class Meta:
        model = models.Admin
        fields = ['username']


class AdminResetPasswordForm(AdminModelForm):
    class Meta:
        model = models.Admin
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

def list_admin(request):
    '''
    管理员账户展示页面
    :param request:
    :return:
    '''
    search = request.GET.get('q', None)
    print(request.headers)
    if search:
        res = models.Admin.objects.filter(Q(username__icontains=search))
        return render(request, 'admin_list.html', {'page_queryset': res})

    queryset = models.Admin.objects.all()
    return render(request, 'admin_list.html', {'page_queryset': queryset})


def add_admin(request):
    '''
    添加管理员账户
    :param request:
    :return:
    '''
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, 'title': '新建管理员'})

    form = AdminModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form': form, 'title': '新建管理员'})


def reset_pwd(request, nid):
    '''
    重置密码
    :param request:
    :param nid: 管理员账户对应的ID
    :return:
    '''
    obj = models.Admin.objects.get(id=nid)
    if request.method == "GET":
        form = AdminResetPasswordForm()
        return render(request, 'change.html', {'form': form, 'title': '重置密码'})

    form = AdminResetPasswordForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form': form, 'title': '重置密码'})


def delete_admin(request):
    '''
    删除管理员账户
    :param request:
    :return:
    '''
    nid = request.GET.get('nid', None)
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def edit_admin(request, nid):
    '''
    编辑管理员账户信息
    :param request:
    :param nid: 管理员id
    :return:
    '''
    obj = models.Admin.objects.get(id=nid)
    if request.method == "GET":
        form = AdminEditModelForm(instance=obj)
        return render(request, 'change.html', {'form': form, 'title': '编辑管理员'})

    form = AdminEditModelForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form': form, 'title': '编辑管理员'})

