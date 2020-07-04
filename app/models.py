from django.db import models
from datetime import date
from django.conf import settings

class CategoryData(models.Model):
	Category_ID=models.CharField(max_length=100, primary_key=True)
	Category_Name=models.CharField(max_length=100)
	Category_Image=models.FileField(upload_to='categoryimage/')
	class Meta:
		db_table="CategoryData"

class NewsletterData(models.Model):
	Email=models.CharField(max_length=100)
	class Meta:
		db_table="NewsletterData"

class SubCategoryData(models.Model):
	SubCategory_ID=models.CharField(max_length=100, primary_key=True)
	Category_ID=models.CharField(max_length=100)
	SubCategory_Name=models.CharField(max_length=100)
	class Meta:
		db_table="SubCategoryData"

class ClassifiedData(models.Model):
	AD_ID=models.CharField(max_length=100, primary_key=True)
	AD_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
	AD_Category=models.CharField(max_length=20)
	City=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Phone=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	Title=models.CharField(max_length=100)
	Price=models.CharField(max_length=50, default='100')
	Description=models.CharField(max_length=500)
	class Meta:
		db_table="ClassifiedData"

class ClassifiedImagesData(models.Model):
	AD_ID=models.CharField(max_length=100)
	Images=models.FileField(upload_to='classifiedimages/')
	class Meta:
		db_table="ClassifiedImagesData"

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
	Post_ID=models.CharField(max_length=100)
	class Meta:
		db_table="UserLeadsData"

class BlogData(models.Model):
	Blog_Date=models.CharField(max_length=100, default=date.today().strftime("%d/%m/%Y"))
	Blog_ID=models.CharField(max_length=100, primary_key=True)
	User_ID=models.CharField(max_length=100, default='Admin')
	Title=models.CharField(max_length=100)
	Body=models.CharField(max_length=1000)
	Image=models.FileField(upload_to='BlogImages/')
	class Meta:
		db_table="BlogData"

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
	Business_Days=models.CharField(max_length=1000, default='Not Availiable')
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

class BusinessAdBannerData(models.Model):
	Business_ID=models.CharField(max_length=100)
	Banner=models.FileField(upload_to='BusinessAdBanner/')
	class Meta:
		db_table="BusinessAdBannerData"

class BusinessReviewData(models.Model):
	Review_ID=models.CharField(max_length=100, primary_key=True)
	Business_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100, default='Unknown')
	Review=models.CharField(max_length=500)
	Rating=models.CharField(max_length=5)
	class Meta:
		db_table="BusinessReviewData"

class BusinessReviewReplyData(models.Model):
	Review_ID=models.CharField(max_length=100)
	Reply=models.CharField(max_length=500)
	class Meta:
		db_table="BusinessReviewReplyData"

class PlanData(models.Model):
	Plan_ID=models.CharField(max_length=10, primary_key=True)
	BusinessListing=models.CharField(max_length=10)
	Ads=models.CharField(max_length=10)
	Map=models.CharField(max_length=10)
	Contact=models.CharField(max_length=10)
	Logo=models.CharField(max_length=10)
	AdBanner=models.CharField(max_length=10)
	URL=models.CharField(max_length=10)
	SocialMedia=models.CharField(max_length=10)
	Product=models.CharField(max_length=10)
	BusinessHours=models.CharField(max_length=10)
	ImageGallery=models.CharField(max_length=10)
	TopBanner=models.CharField(max_length=10)
	Verified=models.CharField(max_length=10)
	UserChat=models.CharField(max_length=10)
	Review=models.CharField(max_length=10)
	Blog=models.CharField(max_length=10)
	Lead=models.CharField(max_length=10, default='1')
	class Meta:
		db_table="PlanData"

class PlanSubscribeData(models.Model):
	Join_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
	Plan_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	class Meta:
		db_table="PlanSubscribeData"

class PaymentData(models.Model):
	Pay_ID=models.CharField(max_length=100, primary_key=True)
	Plan_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	class Meta:
		db_table="PaymentData"

class PaymentData2(models.Model):
	Pay_ID=models.CharField(max_length=100)
	CURRENCY=models.CharField(max_length=100, default='None', blank=True)
	GATEWAYNAME=models.CharField(max_length=100, default='None', blank=True)
	RESPMSG=models.CharField(max_length=1000, default='None', blank=True)
	BANKNAME=models.CharField(max_length=100, default='None', blank=True)
	PAYMENTMODE=models.CharField(max_length=100, default='None', blank=True)
	RESPCODE=models.CharField(max_length=100, default='None', blank=True)
	TXNID=models.CharField(max_length=100, default='None', blank=True)
	TXNAMOUNT=models.CharField(max_length=100, default='None', blank=True)
	STATUS=models.CharField(max_length=100, default='None', blank=True)
	BANKTXNID=models.CharField(max_length=100, default='None', blank=True)
	TXNDATE=models.CharField(max_length=100, default='None', blank=True)
	CHECKSUMHASH=models.CharField(max_length=100, default='None', blank=True)
	class Meta:
		db_table="PaymentData2"

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
	Customer_Message=models.CharField(max_length=1000)
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