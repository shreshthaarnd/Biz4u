from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
import uuid
from app.myutil import *
# Create your views here.
def blog(request):
	return render(request,'blog.html',{})
def cart(request):
	return render(request,'cart.html',{})
def category(request):
	subcategory=request.GET.get('subcategory')
	subcategoryid=''
	categoryid=''
	dic={}
	lt=[]
	obj=SubCategoryData.objects.filter(SubCategory_Name=subcategory)
	for x in obj:
		subcategoryid=x.SubCategory_ID
		categoryid=x.Category_ID
		break
	obj=BusinessData.objects.filter(SubCategory_ID=subcategoryid)
	lt=GetCategoryBusiness(obj)
	subdata=SubCategoryData.objects.filter(Category_ID=categoryid)
	dic={'name':subcategory,'subdata':subdata,'data':lt,'categories':CategoryData.objects.all()}
	dic.update(GetSubCategories())
	return render(request,'category.html',dic)
def checkout(request):
	return render(request,'checkout.html',{})
def contact(request):
	return render(request,'contact.html',{})
def confirmation(request):
	return render(request,'confirmation.html',{})
def elements(request):
	return render(request,'elements.html',{})
def index(request):
	dic=GetSubCategories()
	return render(request,'index.html', dic)
def singleblog(request):
	return render(request,'single-blog.html',{})
def singleproduct(request):
	return render(request,'single-product.html',{})
def login(request):
	return render(request,'login.html',{})
def registration(request):
	return render(request,'registration.html',{})
def tracking(request):
	return render(request,'tracking.html',{})
def postadd(request):
	return render(request,'postadd.html',{})
def sellads(request):
	return render(request,'sellads.html',{})
def rentads(request):
	return render(request,'rentads.html',{})
def adminnavbar(request):
	return render(request,'adminpages/_navbar.html',{})
def adminindex(request):
	return render(request,'adminpages/index.html',{})
def adminsidebar(request):
	return render(request,'adminpages/_sidebar.html',{})
def adminbasicelements(request):
	return render(request,'adminpages/basic_elements.html',{})
def adminbasictable(request):
	return render(request,'adminpages/basic-table.html',{})
def adminblankpage(request):
	return render(request,'adminpages/blank-page.html',{})
def adminbuttons(request):
	return render(request,'adminpages/buttons.html',{})
def adminchartjs(request):
	return render(request,'adminpages/chartjs.html',{})
def admindropdowns(request):
	return render(request,'adminpages/dropdowns.html',{})
def adminerror404(request):
	return render(request,'adminpages/error-404.html',{})
def adminerror500(request):
	return render(request,'adminpages/error-500.html',{})
def adminfontawesome(request):
	return render(request,'adminpages/font-awesome.html',{})
def adminlogin(request):
	return render(request,'adminpages/login.html',{})
def adminregister(request):
	return render(request,'adminpages/register.html',{})
def admintypography(request):
	return render(request,'adminpages/typography.html',{})
def listbusiness(request):
	obj=CategoryData.objects.all()
	dic={'data':obj}
#	obj=BusinessData.objects.all().delete()
	return render(request,'listbusiness.html',dic)
@csrf_exempt
def savebusiness(request):
	if request.method=='POST':
		category=request.POST.get('businesscategory')
		bname=request.POST.get('bname')
		oname=request.POST.get('oname')
		mobile=request.POST.get('mobile')
		email=request.POST.get('email')
		adhaar=request.FILES['adhaar']
		b="B00"
		x=1
		bid=b+str(x)
		while BusinessData.objects.filter(Business_ID=bid).exists():
			x=x+1
			bid=b+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, bname+bid+oname+category+mobile+email)
		password=str(otp)
		password=password.upper()[0:8]
		obj=BusinessData(
			Business_ID=bid,
			Category_ID=category,
			Business_Name=bname,
			Owner_Name=oname,
			Mobile=mobile,
			Email=email,
			Password=password,
			Business_Adhaar=adhaar
		)
		if BusinessData.objects.filter(Business_Name=bname,Email=email).exists():
			obj=CategoryData.objects.all()
			dic={'data':obj,'msg':'Business Already Exists'}
			return render(request,'listbusiness.html',dic)
		else:
			obj.save()
			request.session['business_id'] = bid
			dic={'data':SubCategoryData.objects.filter(Category_ID=category)}
			return render(request,'listbusiness2.html',dic)
	else:
		return redirect('/error404/')
@csrf_exempt
def savebusinessdocument(request):
	if request.method=='POST':
		sub=request.POST.get('subcategory')
		obj=BusinessData.objects.filter(Business_ID=request.session['business_id'])
		obj.update(
			SubCategory_ID=sub
		)
		msg=''
		email=''
		for x in obj:
			email=x.Email
			msg='''Hi '''+x.Owner_Name+'''!
Your business account has been created on Biz4u,

Business Name : '''+x.Business_Name+'''
Business Password : '''+x.Password+'''

Thanks & Regards,
Team Biz4u'''
		sub='Biz4u - Business Account Created'
		email=EmailMessage(sub,msg,to=[email])
		email.send()
		dic={'msg':'A mail has been sent to you with your password,<br>please check your mail!'}
		return render(request,'login.html',dic)
	else:
		return redirect('/error404/')

@csrf_exempt
def logincheck(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('pass')
		if BusinessData.objects.filter(Email=email,Password=password).exists():
			obj=BusinessData.objects.filter(Email=email,Password=password)
			for x in obj:
				request.session['businessid'] = x.Business_ID
				break
			return redirect('/openbusinessdash/')
		else:
			return redirect('/error404/')
def openbusinessdash(request):
	try:
		bid=request.session['businessid']
		return render(request,'business/index.html',{})
	except:
		return redirect('/error404/')

def addservice(request):
	try:
		bid=request.session['businessid']
		return render(request,'business/addservice.html',{})
	except:
		return redirect('/error404/')
@csrf_exempt
def saveservice(request):
#	try:
		bid=request.session['businessid']
		if request.method=='POST':
			name=request.POST.get('name')
			des=request.POST.get('des')
			price=request.POST.get('price')
			imageslt=request.FILES.getlist('images')
			s="S00"
			x=1
			sid=s+str(x)
			while ServicesData.objects.filter(Service_ID=sid).exists():
				x=x+1
				sid=s+str(x)
			x=int(x)
			obj=ServicesData(
				Service_ID=sid,
				Business_ID=bid,
				Service_Name=name,
				Service_Description=des,
				Service_Price=price
			)
			for y in imageslt:
				obj2=ServicesImagesData(
					Service_ID=sid,
					Service_Image=y
				)
				obj2.save()
			if ServicesData.objects.filter(Service_Name=name).exists():
				obj3=ServicesData.objects.filter(Service_ID=sid).delete()
				msg='Product/Service Already Exists'
				return render(request,'business/addservice.html',{'msg':msg})
			else:
				obj.save()
				msg='Product/Service Saved Successfully'
				return render(request,'business/addservice.html',{'msg':msg})
		else:
			return redirect('/error404/')
#	except:
		return redirect('/error404/')

def serviceslist(request):
	try:
		bid=request.session['businessid']
		obj=ServicesData.objects.filter(Business_ID=request.session['businessid'])
		return render(request,'business/serviceslist.html',{'data':obj})
	except:
		return redirect('/error404/')
def deleteservice(request):
	try:
		bid=request.session['businessid']
		obj=ServicesData.objects.filter(Service_ID=request.GET.get('sid')).delete()
		obj=ServicesImagesData.objects.filter(Service_ID=request.GET.get('sid')).delete()
		obj=ServicesData.objects.filter(Business_ID=request.session['businessid'])
		return render(request,'business/serviceslist.html',{'data':obj})
	except:
		return redirect('/error404/')
def changebusinesspassword(request):
	try:
		bid=request.session['businessid']
		return render(request,'business/changebusinesspassword.html',{})
	except:
		return redirect('/error404/')
@csrf_exempt
def savebusinesspassword(request):
	try:
		bid=request.session['businessid']
		if request.method=='POST':
			old=request.POST.get('old')
			new=request.POST.get('new')
			print(old)
			obj=BusinessData.objects.filter(Business_ID=bid)
			if BusinessData.objects.filter(Business_ID=bid, Password=old).exists():
				obj.update(
					Password=new
				)
				msg='Changed Successfully'
				return render(request,'business/changebusinesspassword.html',{'msg':msg})
			else:
				msg='Incorrect Password'
				return render(request,'business/changebusinesspassword.html',{'msg':msg})		
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
def changelogo(request):
	try:
		bid=request.session['businessid']
		obj=BusinessLogoData.objects.filter(Business_ID=bid)
		dic={}
		for x in obj:
			dic={'img':x.Business_Logo.url}
		return render(request,'business/changelogo.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def savelogo(request):
	try:
		bid=request.session['businessid']
		if request.method=='POST':
			logo=request.FILES['logo']
			obj=BusinessLogoData.objects.filter(Business_ID=bid).delete()
			obj=BusinessLogoData(
				Business_ID=bid,
				Business_Logo=logo
				)
			obj.save()
			return redirect('/changelogo/')
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
def businessprofile(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		return render(request,'business/myprofile.html',dic)
	except:
		return redirect('/error404/')

@csrf_exempt
def editbusinessdetails(request):
	try:
		bid=request.session['businessid']
		if request.method=='POST':
			address=request.POST.get('address')
			state=request.POST.get('state')
			city=request.POST.get('city')
			mobile=request.POST.get('mobile')
			obj=BusinessData.objects.filter(Business_ID=bid)
			obj.update(
				Business_Address=address,
				Business_State=state,
				Business_City=city
				)
			return redirect('/businessprofile/')
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
def logout(request):
	try:
		del request.session['businessid']
		request.session.flush()
		return redirect('/index/')
	except:
		return redirect('/index/')
#Admin Code
@csrf_exempt
def adminlogincheck(request):
	if request.method=='POST':
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if e=='admin@biz4u.com' and p=='1234':
			request.session['adminid'] = 'admin@biz4u.com'
			return render(request,'adminpages/index.html',{})
		else:
			return redirect('/error404/')

def defaultcategorieslist(request):
	try:
		adminid=request.session['adminid']
		return render(request,'adminpages/defaultcategorieslist.html',{})
	except:
		return redirect('/error404/')
def addsubcategory(request):
	try:
		adminid=request.session['adminid']
		return render(request,'adminpages/addsubcategory.html',{})
	except:
		return redirect('/error404/')

def addcategory(request):
	'''obj=CategoryData(Category_ID='C001',Category_Name='Home & Office')
	obj.save()
	obj=CategoryData(Category_ID='C002',Category_Name='Home Imporvement')
	obj.save()
	obj=CategoryData(Category_ID='C003',Category_Name='Properties & Rentals')
	obj.save()
	obj=CategoryData(Category_ID='C004',Category_Name='Education & Training')
	obj.save()
	obj=CategoryData(Category_ID='C005',Category_Name='Professional Services')
	obj.save()
	obj=CategoryData(Category_ID='C006',Category_Name='Travel & Transport')
	obj.save()
	obj=CategoryData(Category_ID='C007',Category_Name='Health & Wellness')
	obj.save()
	obj=CategoryData(Category_ID='C008',Category_Name='Events')
	obj.save()'''

@csrf_exempt
def savesubcategory(request):
	if request.method=='POST':
		category=request.POST.get('category')
		subcategory=request.POST.get('subcategory')
		subcategoryimage=request.FILES['subcategoryimage']
		s="SC00"
		x=1
		sid=s+str(x)
		while SubCategoryData.objects.filter(Category_ID=sid).exists():
			x=x+1
			sid=s+str(x)
		x=int(x)
		obj=SubCategoryData(
			SubCategory_ID=sid,
			Category_ID=category,
			SubCategory_Name=subcategory,
			SubCategory_Image=subcategoryimage
			)
		obj.save()
		return render(request,'adminpages/addsubcategory.html',{'msg':'Saved Successfully'})
	else:
		return redirect('/error404/')
def subcategorylist(request):
	try:
		adminid=request.session['adminid']
		obj=SubCategoryData.objects.all()
		lt=reversed(obj)
		return render(request,'adminpages/subcategorylist.html',{'data':lt})
	except:
		return redirect('/error404/')
def deletesubcategory(request):
	try:
		adminid=request.session['adminid']
		obj=SubCategoryData.objects.filter(SubCategory_ID=request.GET.get('sid')).delete()
		return redirect('/subcategorylist/')
	except:
		return redirect('/error404/')