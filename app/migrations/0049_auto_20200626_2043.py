# Generated by Django 2.1.9 on 2020-06-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20200621_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='Blog_Date',
            field=models.CharField(default='26/06/2020', max_length=100),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='Join_Date',
            field=models.CharField(default='26/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='classifieddata',
            name='AD_Date',
            field=models.CharField(default='26/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='plansubscribedata',
            name='Join_Date',
            field=models.CharField(default='26/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='postdata',
            name='Post_Date',
            field=models.CharField(default='26/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Join_Date',
            field=models.CharField(default='26/06/2020', max_length=50),
        ),
    ]
