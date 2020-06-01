from app.models import *

def GetBusinessData(bid):
	obj=BusinessData.objects.filter(Business_ID=bid)
	dic={}
	for x in obj:
		dic={
			'name':x.Business_Name,
			'owner':x.Owner_FName+' '+x.Owner_LName,
			'mobile':x.Business_Mobile,
			'email':x.Business_Email,
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
	for x in obj:
		dic={'name':x.Business_Name,
			'mobile':x.Mobile,
			'city':x.Business_City,
			'address':x.Business_Address,
			'state':x.Business_State}
		obj1=BusinessLogoData.objects.filter(Business_ID=x.Business_ID)
		for y in obj1:
			dic.update({'logo':y.Business_Logo.url})
		lt.append(dic)
	return lt