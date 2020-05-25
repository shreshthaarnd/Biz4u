from django.db import models
import datetime
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class CategoryData(models.Model):
	Category_ID=models.CharField(max_length=100, primary_key=True)
	Category_Name=models.CharField(max_length=100)
	class Meta:
		db_table="CategoryData"

class SubCategoryData(models.Model):
	SubCategory_ID=models.CharField(max_length=100, primary_key=True)
	Category_ID=models.CharField(max_length=100)
	SubCategory_Name=models.CharField(max_length=100)
	SubCategory_Image=models.ImageField(upload_to='subcategoryimage/')
	class Meta:
		db_table="SubCategoryData"

class BusinessData(models.Model):
	Business_ID=models.CharField(max_length=100, primary_key=True)
	Category_ID=models.CharField(max_length=100)
	SubCategory_ID=models.CharField(max_length=100, default='NA')
	Business_Name=models.CharField(max_length=500)
	Owner_Name=models.CharField(max_length=200)
	Mobile=models.CharField(max_length=15)
	Email=models.CharField(max_length=100)
	Password=models.CharField(max_length=50)
	Business_Address=models.CharField(max_length=500, default='Not Availiable')
	Business_City=models.CharField(max_length=100, default='Not Availiable')
	Business_State=models.CharField(max_length=100, default='Not Availiable')
	Business_Adhaar=models.ImageField(upload_to='badhaar/')
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="BusinessData"
class BusinessLogoData(models.Model):
	Business_ID=models.CharField(max_length=100, primary_key=True)
	Business_Logo=models.ImageField(upload_to='blogo/')
	class Meta:
		db_table="BusinessLogoData"

class ServicesData(models.Model):
	Service_ID=models.CharField(max_length=100, primary_key=True)
	Business_ID=models.CharField(max_length=100)
	Service_Name=models.CharField(max_length=200)
	Service_Description=models.CharField(max_length=2000)
	Service_Price=models.CharField(max_length=100)
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="ServicesData"

class ServicesImagesData(models.Model):
	Service_ID=models.CharField(max_length=100, primary_key=True)
	Service_Image=models.ImageField(upload_to='servicesimages/')
	class Meta:
		db_table="ServicesImagesData"