from django.db import models

# Create your models here.


class Department(models.Model):
    # 部门表
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# class Employee(models.Model):
#     # 员工表
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     gender = models.BinaryField()
#     password = models.CharField(max_length=20)
#     salary = models.IntegerField(default=0)
#     create_time = models.DateTimeField(auto_now_add=True)
#     department = models.ForeignKey(Department, to_field='id', on_delete=models.CASCADE)
