from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from utils.md5 import md5
from utils.captcha import check_code
from adminpage import models
from io import BytesIO


# Create your views here.
class LoginForm(forms.Form):
    '''
    登录页面用户名和密码
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        label="用户名",
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        label="密码",
        required=True
    )

    code = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        label="验证码",
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data['password']
        return md5(pwd)


def login(request):
    '''
    登录页面cgi
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(request.POST)
    if form.is_valid():
        input_code = form.cleaned_data.pop('code')
        code = request.session.get('code', None)
        if code != input_code:
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})

        obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if obj:
            # 写入cookie和session
            request.session['info'] = {'username': obj.username}
            return redirect('/admin/list/')

    form.add_error("password", "用户名或密码错误")
    return render(request, 'login.html', {'form': form})


def logout(request):
    """
    退出
    :param request:
    :return:
    """
    request.session.clear()
    return redirect('/login/')


def captcha(request):
    """
    生成验证码
    :param request:
    :return:
    """
    img, code_string = check_code()
    print(code_string)
    stream = BytesIO()
    img.save(stream, format='png')
    stream.getvalue()

    request.session['code'] = code_string

    return HttpResponse(stream.getvalue(), content_type='image/png')

