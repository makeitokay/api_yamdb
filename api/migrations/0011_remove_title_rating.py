# Generated by Django 3.0.5 on 2020-04-27 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_auto_20200427_1809"),
    ]

    operations = [
        migrations.RemoveField(model_name="title", name="rating",),
    ]