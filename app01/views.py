from django.shortcuts import render,redirect
from app01 import models
# Create your views here.


def depart_list(request):
    res = models.Department.objects.all()

    return render(request, 'depart_list.html', {'page_queryset': res})


def depart_add(request):
    if request.method == "POST":
        title = request.POST['title']
        models.Department.objects.create(title=title)
        return redirect('/depart/list')

    return render(request, 'depart_add.html')


def depart_delete(request):
    nid = request.GET['nid']
    models.Department.objects.get(id=nid).delete()

    return redirect('/depart/list')


def depart_edit(request, nid):
    if request.method == "POST":
        title = request.POST['title']
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect('/depart/list')
    title = models.Department.objects.get(id=nid).title
    return render(request, 'depart_edit.html', {'title': title})

