# Generated by Django 2.1.9 on 2020-06-03 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_calldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calldata',
            name='Service_ID',
        ),
    ]
