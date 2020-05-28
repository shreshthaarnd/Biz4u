# Generated by Django 2.1.1 on 2020-05-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_categorydata_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesslogodata',
            name='Business_Logo',
            field=models.FileField(upload_to='blogo/'),
        ),
        migrations.AlterField(
            model_name='categorydata',
            name='Category_Image',
            field=models.FileField(upload_to='categoryimage/'),
        ),
        migrations.AlterField(
            model_name='servicesimagesdata',
            name='Service_Image',
            field=models.FileField(upload_to='servicesimages/'),
        ),
        migrations.AlterField(
            model_name='subcategorydata',
            name='SubCategory_Image',
            field=models.FileField(upload_to='subcategoryimage/'),
        ),
    ]
