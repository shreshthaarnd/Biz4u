# Generated by Django 2.1.9 on 2020-06-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20200619_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'NewsletterData',
            },
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='Blog_Date',
            field=models.CharField(default='21/06/2020', max_length=100),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='Join_Date',
            field=models.CharField(default='21/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='classifieddata',
            name='AD_Date',
            field=models.CharField(default='21/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='plansubscribedata',
            name='Join_Date',
            field=models.CharField(default='21/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='postdata',
            name='Post_Date',
            field=models.CharField(default='21/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='Join_Date',
            field=models.CharField(default='21/06/2020', max_length=50),
        ),
    ]
