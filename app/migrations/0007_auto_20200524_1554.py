# Generated by Django 2.1.1 on 2020-05-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200524_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdata',
            name='Business_Adhaar',
            field=models.ImageField(default='logo.png', upload_to='businessadhaar/'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='Business_Logo',
            field=models.ImageField(default='logo.png', upload_to='businesslogo/'),
        ),
    ]
