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