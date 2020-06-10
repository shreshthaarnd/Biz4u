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
	Join_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
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

class UserLeadsData(models.Model):
	User_ID=models.CharField(max_length=100)
	Post_ID=models.CharField(max_length=100, primary_key=True)
	class Meta:
		db_table="UserLeadsData"

class BusinessData(models.Model):
	Join_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
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
	Business_Hours=models.CharField(max_length=1000, default='Not Availiable')
	Status=models.CharField(max_length=50, default='Active')
	VerifyBadge=models.CharField(max_length=50, default='Unverified')
	class Meta:
		db_table="BusinessData"

class BusinessLogoData(models.Model):
	Business_ID=models.CharField(max_length=100, primary_key=True)
	Business_Logo=models.FileField(upload_to='logo/')
	class Meta:
		db_table="BusinessLogoData"

class BusinessSocialMediaData(models.Model):
	Business_ID=models.CharField(max_length=100)
	Facebook=models.CharField(max_length=200)
	Instagram=models.CharField(max_length=200)
	Twitter=models.CharField(max_length=200)
	class Meta:
		db_table="BusinessSocialMediaData"

class BusinessMapsData(models.Model):
	Business_ID=models.CharField(max_length=100)
	Maps=models.CharField(max_length=1000)
	class Meta:
		db_table="BusinessMapsData"

class BusinessImagesData(models.Model):
	Business_ID=models.CharField(max_length=100)
	Image=models.FileField(upload_to='BusinessImageGallery/')
	class Meta:
		db_table="BusinessImagesData"

class BusinessTopBannerData(models.Model):
	Business_ID=models.CharField(max_length=100)
	Banner=models.FileField(upload_to='BusinessTopBanner/')
	class Meta:
		db_table="BusinessTopBannerData"

class ServicesData(models.Model):
	Service_ID=models.CharField(max_length=100, primary_key=True)
	Business_ID=models.CharField(max_length=100)
	Service_Name=models.CharField(max_length=200)
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="ServicesData"

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