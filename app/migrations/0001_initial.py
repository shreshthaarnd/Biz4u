# Generated by Django 2.1.9 on 2020-05-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_ID', models.CharField(max_length=100)),
                ('Category_Name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'CategoryData',
            },
        ),
    ]
