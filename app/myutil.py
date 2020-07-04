from app.models import *
from django.http import HttpResponse
import csv

def checktrialvalidity(uid):
	userjoin=''
	obj=UserData.objects.filter(User_ID=uid)
	for x in obj:
		userjoin=x.Join_Date
	jday=userjoin[0:2]
	jmonth=userjoin[3:5]
	jyear=userjoin[6:10]
	today=date.today()
	delta=today - date(int(jyear), int(jmonth), int(jday))
	days=delta.days
	if days >= 90:
		return 'Valid'
	else:
		return 'Expired'
def GetBusinessData(bid):
	obj=BusinessData.objects.filter(Business_ID=bid)
	dic={}
	for x in obj:
		dic={
			'name':x.Business_Name,
			'owner':x.Contact_Name,
			'mobile':x.Contact_Number,
			'email':x.Contact_Email,
			'address':x.Business_Address,
			'city':x.Business_City,
			'state':x.Business_State,
			'category':x.Category_Name,
			'subcategory':x.SubCategory_Name
		}
		obj4=BusinessLogoData.objects.filter(Business_ID=x.Business_ID)
		for w in obj4:
			dic.update({'logo':w.Business_Logo.url})
	return dic

def GetRating(bid):
	obj=BusinessReviewData.objects.filter(Business_ID=bid)
	rating=0
	for x in obj:
		rating=rating+int(x.Rating)
	if len(obj) == 0:
		rating=0
	else:
		rating=rating/len(obj)
	return round(rating, 1)

def GetCategoryBusiness(obj):
	lt=[]
	l=[]
	for x in obj:
		dic={'id':x.Business_ID,
			'name':x.Business_Name,
			'scategory':x.SubCategory_Name,
			'mobile':x.Contact_Number,
			'city':x.Business_City,
			'address':x.Business_Address,
			'state':x.Business_State,
			'rating':GetRating(x.Business_ID),
			'verifybadge':GetVerifyBadge(x.Business_ID)}
		obj1=BusinessLogoData.objects.filter(Business_ID=x.Business_ID)
		for y in obj1:
			dic.update({'logo':y.Business_Logo.url})
		obj2=ServicesData.objects.filter(Business_ID=x.Business_ID)
		lt.append(dic)
	return lt
def GetSearchResult(ids):
	lt=[]
	l=[]
	for z in ids:
		obj=BusinessData.objects.filter(Business_ID=z)
		for x in obj:
			dic={'id':x.Business_ID,
				'name':x.Business_Name,
				'mobile':x.Contact_Number,
				'city':x.Business_City,
				'address':x.Business_Address,
				'state':x.Business_State,
				'rating':GetRating(x.Business_ID),
				'category':x.SubCategory_Name,
				'verifybadge':GetVerifyBadge(x.Business_ID)}
			obj1=BusinessLogoData.objects.filter(Business_ID=x.Business_ID)
			for y in obj1:
				dic.update({'logo':y.Business_Logo.url})
			obj2=ServicesData.objects.filter(Business_ID=x.Business_ID)
			lt.append(dic)
	return lt
def checksession(request):
	try:
		uid=request.session['userid']
		return True
	except:
		return False
def unique(list1):
	lt=[]
	list_set = set(list1)
	unique_list = (list(list_set))
	for x in unique_list:
		lt.append(x)
	return lt

def getcities():
	lt=[]
	obj=BusinessData.objects.all()
	for x in obj:
		lt.append(x.Business_City.capitalize())
	return unique(lt)

def GetLeads():
	dic={}
	lt=[]
	for x in PostData.objects.all():
		dic={'Post_ID':x.Post_ID,
			'Post_Date':x.Post_Date,
			'Post_Title':x.Post_Title,
			'Post_Description':x.Post_Description}
		dic.update(GetBusinessData(x.Business_ID))
		lt.append(dic)
	return lt

def GetPlanID(uid):
	planid=''
	obj=PlanSubscribeData.objects.filter(User_ID=uid)
	for x in obj:
		planid=x.Plan_ID
	return planid

from datetime import date
def GetVerifyBadge(bid):
	try:
		uid=''
		joindate=''
		obj=BusinessData.objects.filter(Business_ID=bid)
		for x in obj:
			uid=x.User_ID
		obj=PlanSubscribeData.objects.filter(User_ID=uid)
		for x in obj:
			joindate=x.Join_Date
		jday=joindate[0:2]
		jmonth=joindate[3:5]
		jyear=joindate[6:10]
		planid=GetPlanID(uid)
		today=date.today()
		delta=today - date(int(jyear), int(jmonth), int(jday))
		days=delta.days
		if planid == 'PL002' and days <= 30:
			return True
		elif planid == 'PL003' and days <= 30:
			return True
		else:
			return False
	except:
		days=0
		if planid == 'PL002' and days <= 30:
			return True
		elif planid == 'PL003' and days <= 30:
			return True
		else:
			return False

def GetFeaturedListing():
	dic={}
	lt=[]
	obj=BusinessData.objects.all()
	for x in obj:
		if GetVerifyBadge(x.Business_ID):
			dic={
			'id':x.Business_ID,
			'name':x.Business_Name,
			'category':x.Category_Name
			}
			for y in BusinessLogoData.objects.filter(Business_ID=x.Business_ID):
				dic.update({
					'logo':y.Business_Logo.url
					})
			lt.append(dic)
	return reversed(lt)

def GetBusinessReviews(bid):
	dic={}
	lt=[]
	obj=BusinessReviewData.objects.filter(Business_ID=bid)
	for x in obj:
		dic={
		'review':x.Review
		}
		for y in UserData.objects.filter(User_ID=x.User_ID):
			dic.update({
				'name':y.User_FName+' '+y.User_LName
				})
		lt.append(dic)
	return reversed(lt)

def GetClassidieds():
	dic={}
	lt=[]
	obj=ClassifiedData.objects.all()
	for x in obj:
		dic={'category':x.AD_Category,
			'title':x.Title,
			'id':x.AD_ID,
			'date':x.AD_Date}
		for y in ClassifiedImagesData.objects.filter(AD_ID=x.AD_ID):
			dic.update({
				'image':y.Images.url
				})
			break
		lt.append(dic)
	return lt

def downloadCSV(table):
	if table=='CategoryData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=CategoryData.csv'
		writer = csv.writer(response)
		writer.writerow(["Category_ID", "Category_Name", "Category_Image"])
		obj1=CategoryData.objects.all()
		for x in obj1:
			writer.writerow([x.Category_ID, x.Category_Name, x.Category_Image])
		return response
	if table=='NewsletterData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=NewsletterData.csv'
		writer = csv.writer(response)
		writer.writerow(["Email"])
		obj1=NewsletterData.objects.all()
		for x in obj1:
			writer.writerow([x.Email])
		return response
	if table=='SubCategoryData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=SubCategoryData.csv'
		writer = csv.writer(response)
		writer.writerow(["SubCategory_ID", "Category_ID", "SubCategory_Name"])
		obj1=SubCategoryData.objects.all()
		for x in obj1:
			writer.writerow([x.SubCategory_ID, x.Category_ID, x.SubCategory_Name])
		return response
	if table=='ClassifiedData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=ClassifiedData.csv'
		writer = csv.writer(response)
		writer.writerow(["AD_ID", "AD_Date", "AD_Category", "City", "Email", "Phone", "Name", "Title", "Price", "Description"])
		obj1=ClassifiedData.objects.all()
		for x in obj1:
			writer.writerow([x.AD_ID, x.AD_Date, x.AD_Category, x.City, x.Email, x.Phone, x.Name, x.Title, x.Price, x.Description])
		return response
	if table=='ClassifiedImagesData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=ClassifiedImagesData.csv'
		writer = csv.writer(response)
		writer.writerow(["AD_ID", "Images"])
		obj1=ClassifiedImagesData.objects.all()
		for x in obj1:
			writer.writerow([x.AD_ID, x.Images])
		return response
	if table=='UserData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=UserData.csv'
		writer = csv.writer(response)
		writer.writerow(["Join_Date", "User_ID", "User_FName", "User_LName", "User_Mobile", "User_Email", "User_Password", "Verify_Status", "Account_Status"])
		obj1=UserData.objects.all()
		for x in obj1:
			writer.writerow([x.Join_Date, x.User_ID, x.User_FName, x.User_LName, x.User_Mobile, x.User_Email, x.User_Password, x.Verify_Status, x.Account_Status])
		return response
	if table=='UserLeadsData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=UserLeadsData.csv'
		writer = csv.writer(response)
		writer.writerow(["User_ID", "Post_ID"])
		obj1=UserLeadsData.objects.all()
		for x in obj1:
			writer.writerow([x.User_ID, x.Post_ID])
		return response
	if table=='BlogData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BlogData.csv'
		writer = csv.writer(response)
		writer.writerow(["Blog_Date", "Blog_ID", "User_ID", "Title", "Body", "Image"])
		obj1=BlogData.objects.all()
		for x in obj1:
			writer.writerow([x.Blog_Date, x.Blog_ID, x.User_ID, x.Title, x.Body, x.Image])
		return response
	if table=='BusinessData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessData.csv'
		writer = csv.writer(response)
		writer.writerow(["Join_Date", "Business_ID", "User_ID", "User_ID", "Contact_Name", "Contact_Number", "Contact_Email", "Category_Name", "SubCategory_Name", "Business_Address", "Business_City", "Business_State", "Business_Website", "Business_Decription", "Business_Hours", "Business_Days", "Status", "VerifyBadge"])
		obj1=BusinessData.objects.all()
		for x in obj1:
			writer.writerow([x.Join_Date, x.Business_ID, x.User_ID, x.User_ID, x.Contact_Name, x.Contact_Number, x.Contact_Email, x.Category_Name, x.SubCategory_Name, x.Business_Address, x.Business_City, x.Business_State, x.Business_Website, x.Business_Decription, x.Business_Hours, x.Business_Days, x.Status, x.VerifyBadge])
		return response
	if table=='BusinessLogoData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessLogoData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Business_Logo"])
		obj1=BusinessLogoData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Business_Logo])
		return response
	if table=='BusinessSocialMediaData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessSocialMediaData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Facebook", "Instagram", "Twitter"])
		obj1=BusinessSocialMediaData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Facebook, x.Instagram, x.Twitter])
		return response
	if table=='BusinessMapsData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessMapsData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Maps"])
		obj1=BusinessMapsData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Maps])
		return response
	if table=='BusinessImagesData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessImagesData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Image"])
		obj1=BusinessImagesData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Image])
		return response
	if table=='BusinessTopBannerData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessTopBannerData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Banner"])
		obj1=BusinessTopBannerData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Banner])
		return response
	if table=='BusinessAdBannerData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessAdBannerData.csv'
		writer = csv.writer(response)
		writer.writerow(["Business_ID", "Banner"])
		obj1=BusinessAdBannerData.objects.all()
		for x in obj1:
			writer.writerow([x.Business_ID, x.Banner])
		return response
	if table=='BusinessReviewData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessReviewData.csv'
		writer = csv.writer(response)
		writer.writerow(["Review_ID", "Business_ID", "User_ID", "Review", "Rating"])
		obj1=BusinessReviewData.objects.all()
		for x in obj1:
			writer.writerow([x.Review_ID, x.Business_ID, x.User_ID, x.Review, x.Rating])
		return response
	if table=='BusinessReviewReplyData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=BusinessReviewReplyData.csv'
		writer = csv.writer(response)
		writer.writerow(["Review_ID", "Reply"])
		obj1=BusinessReviewReplyData.objects.all()
		for x in obj1:
			writer.writerow([x.Review_ID, x.Reply])
		return response
	if table=='PlanData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=PlanData.csv'
		writer = csv.writer(response)
		writer.writerow(["Plan_ID", "BusinessListing", "Ads", "Map", "Contact", "Logo", "AdBanner", "URL", "SocialMedia", "Product", "BusinessHours", "TopBanner", "Verified", "UserChat", "Review", "Blog", "Lead"])
		obj1=PlanData.objects.all()
		for x in obj1:
			writer.writerow([x.Plan_ID, x.BusinessListing, x.Ads, x.Map, x.Contact, x.Logo, x.AdBanner, x.URL, x.SocialMedia, x.Product, x.BusinessHours, x.TopBanner, x.Verified, x.UserChat, x.Review, x.Blog, x.Lead])
		return response
	if table=='PlanSubscribeData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=PlanSubscribeData.csv'
		writer = csv.writer(response)
		writer.writerow(["Join_Date", "Plan_ID", "User_ID"])
		obj1=PlanSubscribeData.objects.all()
		for x in obj1:
			writer.writerow([x.Join_Date, x.Plan_ID, x.User_ID])
		return response
	if table=='PaymentData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=PaymentData.csv'
		writer = csv.writer(response)
		writer.writerow(["Pay_ID", "Plan_ID", "User_ID"])
		obj1=PaymentData.objects.all()
		for x in obj1:
			writer.writerow([x.Pay_ID, x.Plan_ID, x.User_ID])
		return response
	if table=='PaymentData2':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=PaymentData2.csv'
		writer = csv.writer(response)
		writer.writerow(["Pay_ID", "CURRENCY", "GATEWAYNAME", "RESPMSG", "BANKNAME", "PAYMENTMODE", "RESPCODE", "TXNID", "TXNAMOUNT", "STATUS", "BANKTXNID", "TXNDATE", "CHECKSUMHASH"])
		obj1=PaymentData2.objects.all()
		for x in obj1:
			writer.writerow([x.Pay_ID, x.CURRENCY, x.GATEWAYNAME, x.RESPMSG, x.BANKNAME, x.PAYMENTMODE, x.RESPCODE, x.TXNID, x.TXNAMOUNT, x.STATUS, x.BANKTXNID, x.TXNDATE, x.CHECKSUMHASH])
		return response
	if table=='ServicesData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=ServicesData.csv'
		writer = csv.writer(response)
		writer.writerow(["Service_ID", "Business_ID", "Service_Name", "Status"])
		obj1=ServicesData.objects.all()
		for x in obj1:
			writer.writerow([x.Service_ID, x.Business_ID, x.Service_Name, x.Status])
		return response
	if table=='CallData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=CallData.csv'
		writer = csv.writer(response)
		writer.writerow(["Call_ID", "Business_ID", "Customer_Name", "Customer_Number", "Customer_Message", "Customer_Message"])
		obj1=CallData.objects.all()
		for x in obj1:
			writer.writerow([x.Call_ID, x.Business_ID, x.Customer_Name, x.Customer_Number, x.Customer_Message, x.Customer_Message])
		return response
	if table=='PostData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=PostData.csv'
		writer = csv.writer(response)
		writer.writerow(["Post_Date", "Post_ID", "Business_ID", "User_ID", "Post_Title", "Post_Description"])
		obj1=PostData.objects.all()
		for x in obj1:
			writer.writerow([x.Post_Date, x.Post_ID, x.Business_ID, x.User_ID, x.Post_Title, x.Post_Description])
		return response