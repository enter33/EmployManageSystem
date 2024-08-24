from django.shortcuts import render, redirect
from pretty_num import models
from django import forms
from django.db.models import Q
# Create your views here.


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        fields = '__all__'


def list_pretty_num(request):
    search = request.GET.get('q', None)
    if search:
        res = models.PrettyNum.objects.filter(Q(mobile__icontains=search)).order_by('level')
        return render(request, 'pretty_num_list.html', {'page_queryset': res})

    res = models.PrettyNum.objects.all().order_by('level')
    return render(request, 'pretty_num_list.html', {'page_queryset': res})


def add_pretty_num(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'pretty_num_add.html', {'form': form})

    form = UserModelForm(request.POST)
    if form.is_valid():
        mobile = request.POST.get('mobile')
        if models.PrettyNum.objects.filter(mobile=mobile).exists():
            return redirect('/pretty_num/list/')

        form.save()
        return redirect('/pretty_num/list/')

    return render(request, 'pretty_num_add.html', {'form': form})


def edit_pretty_num(request, nid):
    if request.method == 'GET':
        form = UserModelForm(instance=models.PrettyNum.objects.get(id=nid))
        return render(request, 'pretty_num_edit.html', {'form': form})

    form = UserModelForm(request.POST, instance=models.PrettyNum.objects.get(id=nid))
    if form.is_valid():
        form.save()
        return redirect('/pretty_num/list/')

    return render(request, 'pretty_num_edit.html', {'form': form})


def delete_pretty_num(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.PrettyNum.objects.get(id=nid).delete()
        return redirect('/pretty_num/list/')
