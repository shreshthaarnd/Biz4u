from app.models import *

def GetBusinessData(bid):
	obj=BusinessData.objects.filter(Business_ID=bid)
	dic={}
	for x in obj:
		dic={
			'name':x.Business_Name,
			'owner':x.Owner_Name,
			'mobile':x.Mobile,
			'email':x.Email,
			'adhaar':x.Business_Adhaar.url,
			'address':x.Business_Address,
			'city':x.Business_City,
			'state':x.Business_State,
		}
		obj2=CategoryData.objects.filter(Category_ID=x.Category_ID)
		for y in obj2:
			dic.update({
				'category':y.Category_Name
				})
		obj3=SubCategoryData.objects.filter(SubCategory_ID=x.SubCategory_ID)
		for z in obj3:
			dic.update({
				'subcategory':z.SubCategory_Name
				})
		obj4=BusinessLogoData.objects.filter(Business_ID=x.Business_ID)
		for w in obj4:
			dic.update({
				'logo':w.Business_Logo.url
				})
	return dic
def GetSubCategories():
	lt=[]
	dic={}
	obj=SubCategoryData.objects.filter(Category_ID='C001')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'homeoffice':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C002')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'homeimprovement':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C003')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'propertiesrentals':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C004')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'educationtraining':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C005')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'professionalservice':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C006')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'traveltransport':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C007')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'healthwellness':lt})
	lt=[]
	obj=SubCategoryData.objects.filter(Category_ID='C008')
	for x in obj:
		lt.append(x.SubCategory_Name)
	dic.update({'events':lt})
	lt=[]
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