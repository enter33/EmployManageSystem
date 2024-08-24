from django.db import models
from app01 import models as app01_models


# Create your models here.
class Employee(models.Model):
    # 员工表
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(verbose_name='性别')
    password = models.CharField(max_length=20, verbose_name='密码')
    salary = models.IntegerField(default=0, verbose_name='余额')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    department = models.ForeignKey(app01_models.Department, verbose_name='部门', to_field='id', on_delete=models.CASCADE)
