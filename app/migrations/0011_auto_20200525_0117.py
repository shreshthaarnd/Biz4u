# Generated by Django 2.1.1 on 2020-05-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_servicesdata_servicesimagesdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessLogoData',
            fields=[
                ('Business_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Business_Logo', models.ImageField(upload_to='blogo/')),
            ],
            options={
                'db_table': 'BusinessLogoData',
            },
        ),
        migrations.RemoveField(
            model_name='businessdata',
            name='Business_Logo',
        ),
    ]
