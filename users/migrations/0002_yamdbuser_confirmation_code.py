# Generated by Django 3.0.5 on 2020-04-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yamdbuser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]