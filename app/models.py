from django.db import models
from datetime import date
from django.conf import settings

class CategoryData(models.Model):
	Category_ID=models.CharField(max_length=100, primary_key=True)
	Category_Name=models.CharField(max_length=100)
	Category_Image=models.FileField(upload_to='categoryimage/')
	class Meta:
		db_table="CategoryData"

class SubCategoryData(models.Model):
	SubCategory_ID=models.CharField(max_length=100, primary_key=True)
	Category_ID=models.CharField(max_length=100)
	SubCategory_Name=models.CharField(max_length=100)
	SubCategory_Image=models.FileField(upload_to='subcategoryimage/')
	class Meta:
		db_table="SubCategoryData"

class UserData(models.Model):
	User_ID=models.CharField(max_length=100, primary_key=True)
	User_FName=models.CharField(max_length=100)
	User_LName=models.CharField(max_length=100)
	User_Mobile=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=100)
	User_Password=models.CharField(max_length=100)
	Verify_Status=models.CharField(max_length=100, default='Unverified')
	Account_Status=models.CharField(max_length=100, default='Active')
	class Meta:
		db_table="UserData"

class BusinessData(models.Model):
	Business_ID=models.CharField(max_length=100, primary_key=True)
	User_ID=models.CharField(max_length=100)
	Contact_Name=models.CharField(max_length=100)
	Contact_Number=models.CharField(max_length=100)
	Contact_Email=models.CharField(max_length=100)
	Category_Name=models.CharField(max_length=100)
	SubCategory_Name=models.CharField(max_length=100, default='NA')
	Business_Name=models.CharField(max_length=500)
	Business_Address=models.CharField(max_length=500, default='Not Availiable')
	Business_City=models.CharField(max_length=100, default='Not Availiable')
	Business_State=models.CharField(max_length=100, default='Not Availiable')
	Business_Website=models.CharField(max_length=100, default='Not Availiable')
	Business_Decription=models.CharField(max_length=1000, default='Not Availiable')
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="BusinessData"

class BusinessLogoData(models.Model):
	Business_ID=models.CharField(max_length=100, primary_key=True)
	Business_Logo=models.FileField(upload_to='blogo/')
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
	Service_Image=models.FileField(upload_to='servicesimages/')
	class Meta:
		db_table="ServicesImagesData"

class CallData(models.Model):
	Call_ID=models.CharField(max_length=100, primary_key=True)
	Business_ID=models.CharField(max_length=100)
	Customer_Name=models.CharField(max_length=100)
	Customer_Number=models.CharField(max_length=50)
	class Meta:
		db_table="CallData"

class PostData(models.Model):
	Post_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
	Post_ID=models.CharField(max_length=100, primary_key=True)
	Business_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Post_Title=models.CharField(max_length=100)
	Post_Description=models.CharField(max_length=50)
	class Meta:
		db_table="PostData"