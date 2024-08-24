from django.shortcuts import render, redirect
from user import models
from app01 import models as app01_models
from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ('name', 'age', 'gender', 'password', 'salary', 'department')
# Create your views here.


def user_list(request):
    res = models.Employee.objects.all()
    return render(request, 'user_list.html', {'page_queryset': res})


def user_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        department_id = int(request.POST.get('department'))  # 获取部门的 ID 并转换为整数
        department = app01_models.Department.objects.get(id=department_id)
        create_time = request.POST.get('create_time')

        models.Employee.objects.create(name=name, age=age, salary=salary, password=password,
                                       gender=gender, department=department, create_time=create_time)
        return redirect('/user/list/')

    depart_list = app01_models.Department.objects.all()
    return render(request, 'user_add.html',
                  {'depart_list': depart_list})


def user_delete(request):
    nid = request.GET.get('nid')
    models.Employee.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def user_edit(request, nid):
    row_obj = models.Employee.objects.get(id=nid)
    if request.method == "GET":
        form = UserModelForm(instance=row_obj)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_modelform_add(request):
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/list/')

    return render(request, 'user_model_form_add.html',{'form': form})
