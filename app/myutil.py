from app.models import *

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
	print(rating)
	rating=rating/len(obj)
	return round(rating, 1)

def GetCategoryBusiness(obj):
	lt=[]
	l=[]
	for x in obj:
		dic={'id':x.Business_ID,
			'name':x.Business_Name,
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
	elif planid == 'PL003' and days <= 60:
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