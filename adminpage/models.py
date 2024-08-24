from django.db import models

# Create your models here.


class Admin(models.Model):
    username = models.CharField(max_length=10, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=50, verbose_name='密码')
