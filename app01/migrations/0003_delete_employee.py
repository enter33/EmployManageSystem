# Generated by Django 4.1.2 on 2024-07-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_rename_department_name_department_title"),
    ]

    operations = [
        migrations.DeleteModel(name="Employee",),
    ]