# Generated by Django 2.1.1 on 2020-05-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200525_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydata',
            name='Category_Image',
            field=models.ImageField(default=1, upload_to='categoryimage/'),
            preserve_default=False,
        ),
    ]
