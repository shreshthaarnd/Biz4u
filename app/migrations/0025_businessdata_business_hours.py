# Generated by Django 2.1.9 on 2020-06-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20200610_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdata',
            name='Business_Hours',
            field=models.CharField(default='Not Availiable', max_length=1000),
        ),
    ]
