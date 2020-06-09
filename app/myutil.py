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

def GetCategoryBusiness(obj):
	lt=[]
	l=[]
	for x in obj:
		dic={'id':x.Business_ID,
			'name':x.Business_Name,
			'mobile':x.Contact_Number,
			'city':x.Business_City,
			'address':x.Business_Address,
			'state':x.Business_State}
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
def getcities():
	lt=[]
	obj=BusinessData.objects.all()
	for x in obj:
		lt.append(x.Business_City.upper())
	return lt

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