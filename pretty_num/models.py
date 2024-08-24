from django.db import models

# Create your models here.


class PrettyNum(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    price = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='价格')
    level_choice = (
        (1, "1级"),
        (2, "2级"),
        (3, "4级"),
    )
    level = models.SmallIntegerField(choices=level_choice, verbose_name='级别', default=1)
    status_choice = (
        (1, "已使用"),
        (2, "未使用")
    )
    status = models.IntegerField(choices=status_choice, verbose_name='状态')
