from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
import uuid
from app.myutil import *

def saveplan(request):
	obj=PlanData.objects.all()
	obj=PlanData(
		Plan_ID='PL001',
		BusinessListing='1',
		Ads='1',
		Map='Yes',
		Contact='Yes',
		Logo='Yes',
		AdBanner='No',
		URL='Yes',
		SocialMedia='No',
		Product='No',
		BusinessHours='No',
		ImageGallery='No',
		TopBanner='No',
		Verified='No',
		UserChat='No',
		Review='Yes',
		Blog='No',
		Lead='1',
		)
	obj.save()
	obj=PlanData(
		Plan_ID='PL002',
		BusinessListing='3',
		Ads='3',
		Map='Yes',
		Contact='Yes',
		Logo='Yes',
		AdBanner='1',
		URL='Yes',
		SocialMedia='Yes',
		Product='No',
		BusinessHours='Yes',
		ImageGallery='Yes',
		TopBanner='No',
		Verified='Yes',
		UserChat='Yes',
		Review='Yes',
		Blog='No',
		Lead='50',
		)
	obj.save()
	obj=PlanData(
		Plan_ID='PL003',
		BusinessListing='Unlimited',
		Ads='Unlimited',
		Map='Yes',
		Contact='Yes',
		Logo='Yes',
		AdBanner='2',
		URL='Yes',
		SocialMedia='Yes',
		Product='Yes',
		BusinessHours='Yes',
		ImageGallery='Yes',
		TopBanner='Yes',
		Verified='Yes',
		UserChat='Yes',
		Review='Yes',
		Blog='Yes',
		Lead='Unlimited',
		)
	obj.save()
	obj=PlanSubscribeData(
		Plan_ID='PL001',
		User_ID=request.session['userid']
		)
	obj.save()
	return HttpResponse('Done')
def blog(request):
	try:
		blog=BlogData.objects.all()
		user=UserData.objects.all()
		dic={'blog':reversed(list(blog)),
			'user':user,
			'checksession':checksession(request),
			'plan':request.session['planid']}
		return render(request,'blog.html',dic)
	except:
		blog=BlogData.objects.all()
		user=UserData.objects.all()
		dic={'blog':reversed(list(blog)),
			'user':user,
			'checksession':checksession(request)}
		return render(request,'blog.html',dic)
	
def cart(request):
	return render(request,'cart.html',{})

def category(request):
	subcategory=request.GET.get('subcategory')
	categoryid=''
	dic={}
	lt=[]
	obj=BusinessData.objects.filter(SubCategory_Name=subcategory)
	lt=GetCategoryBusiness(obj)
	subdata=SubCategoryData.objects.filter(SubCategory_Name=subcategory)
	for x in subdata:
		categoryid=x.Category_ID
	subdata=SubCategoryData.objects.filter(Category_ID=categoryid)
	page = request.GET.get('page')
	paginator = Paginator(list(reversed(lt)), 10)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	dic={'name':subcategory,
		'subdata':subdata,
		'data':data,
		'checksession':checksession(request),
		'categories':CategoryData.objects.all()}
	return render(request,'category.html',dic)
@csrf_exempt
def searchresult(request):
	city=request.POST.get('city')
	search=request.POST.get('search')
	lt=[]
	result=[]
	for x in BusinessData.objects.all():
		if x.Business_City.capitalize() == city and x.Business_Name.upper() == search.upper():
			lt.append(x.Business_ID)
	dic={'result':GetSearchResult(lt),
		'checksession':checksession(request),
		'count':len(GetSearchResult(lt)),
		'categories':CategoryData.objects.all()}
	return render(request,'searchresult.html',dic)
def opencity(request):
	city=request.GET.get('city')
	categoryid=''
	dic={}
	lt=[]
	obj=BusinessData.objects.filter(Business_City=city)
	lt=GetCategoryBusiness(obj)
	page = request.GET.get('page')
	paginator = Paginator(list(reversed(lt)), 10)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	dic={'data':data,
		'checksession':checksession(request),
		'cities':getcities(),
		'categories':CategoryData.objects.all()}
	return render(request,'opencity.html',dic)
def contact(request):
	return render(request,'contact.html',{})
def confirmation(request):
	return render(request,'confirmation.html',{})
def elements(request):
	return render(request,'elements.html',{})
def index(request):
	dic={'category':CategoryData.objects.all(),
		'subcategory':SubCategoryData.objects.all(),
		'cities':getcities(),
		'featured':GetFeaturedListing(),
		'ads':GetClassidieds()[0:20],
		'banner':BusinessAdBannerData.objects.all(),
		'checksession':checksession(request)}
	return render(request,'index.html', dic)

def classifieds(request):
	ads=ClassifiedData.objects.all()
	dic={'ads':ads,'images':GetClassidieds(),'checksession':checksession(request),}
	return render(request,'classifiedads.html', dic)

def classifiedsCategories(request):
	category=request.GET.get('category')
	ads=ClassifiedData.objects.filter(AD_Category=category)
	dic={'ads':ads,'images':GetClassidieds(),'checksession':checksession(request),}
	return render(request,'classifiedads.html', dic)

def classifieddetail(request):
	aid=request.GET.get('aid')
	ads=ClassifiedData.objects.filter(AD_ID=aid)
	images=ClassifiedImagesData.objects.all()
	dic={'ads':ads,'images':images,'checksession':checksession(request),}
	return render(request,'classifieddetail.html', dic)

def singleblog(request):
	blog=BlogData.objects.filter(Blog_ID=request.GET.get('bid'))
	user=UserData.objects.all()
	dic={'blog':blog,'user':user,'checksession':checksession(request)}
	return render(request,'single-blog.html',dic)
def singleproduct(request):
	obj=BusinessData.objects.filter(Business_ID=request.GET.get('bid'))
	obj1=BusinessLogoData.objects.filter(Business_ID=request.GET.get('bid'))
	obj2=ServicesData.objects.filter(Business_ID=request.GET.get('bid'))
	obj3=BusinessSocialMediaData.objects.filter(Business_ID=request.GET.get('bid'))
	obj4=BusinessMapsData.objects.filter(Business_ID=request.GET.get('bid'))
	obj5=BusinessImagesData.objects.filter(Business_ID=request.GET.get('bid'))
	obj6=BusinessTopBannerData.objects.filter(Business_ID=request.GET.get('bid'))
	obj7=BusinessReviewData.objects.filter(Business_ID=request.GET.get('bid'))
	verifybadge=GetVerifyBadge(request.GET.get('bid'))
	rating=0
	for x in obj7:
		rating=rating+int(x.Rating)
	rating=rating/len(obj7)
	rating=round(rating, 1)
	dic={'data':obj,
		'logo':obj1,
		'product':obj2,
		'social':obj3,
		'maps':obj4,
		'image':obj5,
		'banner':obj6,
		'rating':rating,
		'reviews':GetBusinessReviews(request.GET.get('bid')),
		'verifybadge':verifybadge,
		'checksession':checksession(request)}
	return render(request,'single-product.html',dic)
@csrf_exempt
def savereview(request):
	if request.method=='POST':
		bid=request.POST.get('bid')
		uid=request.session['userid']
		review=request.POST.get('review')
		star=request.POST.get('star')
		obj=BusinessReviewData()
		r="RE00"
		x=1
		rid=r+str(x)
		while BusinessReviewData.objects.filter(Review_ID=rid).exists():
			x=x+1
			rid=r+str(x)
		x=int(x)
		obj=BusinessReviewData(
			Review_ID=rid,
			Business_ID=bid,
			User_ID=uid,
			Review=review,
			Rating=star
			)
		obj.save()
		return HttpResponse("<script>alert('Thanks for your rating!'); window.location.replace('/singleproduct/?bid="+bid+"')</script>")

def login(request):
	return render(request,'login.html',{})
def forgotpassword(request):
	return render(request,'forgotpassword.html',{})
@csrf_exempt
def sendpassword(request):
	if request.method=='POST':
		email=request.POST.get('email')
		obj=UserData.objects.all()
		for x in obj:
			if x.User_Email == email:
				sub='Addbiz4u Account Password Recovery'
				msg='''Hi there!
Your Addbiz4u Account Password is,

'''+x.User_Password+'''

Thanks!
Team Addbiz4u'''
				email=EmailMessage(sub,msg,to=[x.User_Email])
				email.send()
				return HttpResponse("<script>alert('Password has benn sent to your mail.'); window.location.replace('/login/')</script>")
			else:
				return HttpResponse("<script>alert('Incorrect Password'); window.location.replace('/forgotpassword/')</script>")
			break

def registration(request):
	return render(request,'registration.html',{})
def tracking(request):
	return render(request,'tracking.html',{})
def postadd(request):
	dic={'checksession':checksession(request)}
	return render(request,'postadd.html',dic)
@csrf_exempt
def savead(request):
	if request.method=='POST':
		category=request.POST.get('category')
		city=request.POST.get('city')
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		title=request.POST.get('title')
		des=request.POST.get('description')
		images=request.FILES.getlist('images')
		price=request.FILES.getlist('price')
		a="ADS00"
		x=1
		aid=a+str(x)
		while ClassifiedData.objects.filter(AD_ID=aid).exists():
			x=x+1
			aid=a+str(x)
		x=int(x)
		obj=ClassifiedData(
			AD_ID=aid,
			AD_Category=category,
			City=city,
			Name=name,
			Email=email,
			Phone=phone,
			Title=title,
			Price=price,
			Description=des
			)
		obj.save()
		for x in images:
			obj=ClassifiedImagesData(AD_ID=aid, Images=x).save()
		sub='AddBiz4u Classified Ad Detail'
		msg='''Hi there!
Your Free Classified Advertisement has been published successfully,

AD Credentials:
Email '''+email+''',
AD ID '''+aid+'''

Thanks!
Team Addbiz4u'''
		email=EmailMessage(sub,msg,to=[email])
		email.send()
		return HttpResponse("<script>alert('Ad posted successfully and credentials has been sent to your mail.'); window.location.replace('/index/')</script>")

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
@csrf_exempt
def saveuser2(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		mobile=request.POST.get('mobile')
		email=request.POST.get('email')
		password=request.POST.get('password')
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, fname+lname+uid+mobile+email).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['userotp'] = otp
		obj=UserData(
			User_ID=uid,
			User_FName=fname,
			User_LName=lname,
			User_Mobile=mobile,
			User_Email=email,
			User_Password=password
			)
		if UserData.objects.filter(User_Email=email):
			return HttpResponse("<script>alert('User Already Exists'); window.location.replace('/registration/')</script>")
		else:
			obj.save()
			return HttpResponse("<script>alert('Account Created Successfully, Proceed for Login'); window.location.replace('/login/')</script>")

@csrf_exempt
def saveuser(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		mobile=request.POST.get('mobile')
		email=request.POST.get('email')
		password=request.POST.get('password')
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, fname+lname+uid+mobile+email).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['userotp'] = otp
		obj=UserData(
			User_ID=uid,
			User_FName=fname,
			User_LName=lname,
			User_Mobile=mobile,
			User_Email=email,
			User_Password=password
			)
		if UserData.objects.filter(User_Email=email):
			return HttpResponse("<script>alert('User Already Exists'); window.location.replace('/addbusiness/')</script>")
		else:
			obj.save()
			sub='Biz4u Verification Code'
			msg='''Hi there!
Your Biz4u Verification code is,

'''+otp+'''

Thanks!
Team Biz4u'''
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			dic={'userid':uid}
			return render(request,'addbusiness2.html',dic)
@csrf_exempt
def verifyaccount(request):
	if request.method=='POST':
		uid=request.POST.get('userid')
		otpp=request.POST.get('otp')
		otp=request.session['userotp']
		if otpp == otp:
			obj=UserData.objects.filter(User_ID=uid)
			obj.update(Verify_Status='Verified')
			request.session['userid'] = uid
			obj=PlanSubscribeData(
				Plan_ID='PL001',
				User_ID=uid
				)
			obj.save()
			return redirect('/addbusiness3/')
		else:
			dic={'userid':uid,
				'msg':'Incorrect OTP','checksession':checksession(request),}
			return render(request,'addbusiness2.html',dic)
def resendOTP(request):
	uid=request.GET.get('uid')
	email=''
	obj=UserData.objects.filter(User_ID=uid)
	for x in obj:
		email=x.User_Email
	sub='Biz4u Verification Code'
	msg='''Hi there!
Your Biz4u Verification code is,

'''+request.session["userotp"]+'''

Thanks!
Team Biz4u'''
	email=EmailMessage(sub,msg,to=[email])
	email.send()
	dic={'userid':uid,'checksession':checksession(request),}
	return render(request,'addbusiness2.html',dic)

@csrf_exempt
def logincheck(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('pass')
		if UserData.objects.filter(User_Email=email,User_Password=password).exists():
			if UserData.objects.filter(User_Email=email,Verify_Status='Verified').exists():
				for x in UserData.objects.filter(User_Email=email):
					request.session['userid']=x.User_ID
					break
				return redirect('/userdashboard/')
			else:
				uid=''
				for x in UserData.objects.filter(User_Email=email):
					uid=x.User_ID
				return redirect('/resendOTP/?uid='+uid)
		else:
			return HttpResponse("<script>alert('Incorrect Email ID/Password'); window.location.replace('/login/')</script>")
def userdashboard(request):
	print(request.session['userid'])
	obj=UserData.objects.filter(User_ID=request.session['userid'])
	obj2=BusinessData.objects.filter(User_ID=request.session['userid'])
	plan=''
	obj1=PlanSubscribeData.objects.filter(User_ID=request.session['userid'])
	for x in obj1:
		plan=x.Plan_ID
	request.session['planid'] = plan
	dic={'data':obj,'data2':obj2,'plan':plan,'checksession':checksession(request),}
	return render(request,'userdashboard.html',dic)
@csrf_exempt
def edituserdata(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		mobile=request.POST.get('mobile')
		obj=UserData.objects.filter(User_ID=request.session['userid'])
		obj.update(
			User_FName=fname,
			User_LName=lname,
			User_Mobile=mobile
			)
		return redirect('/userdashboard/')
@csrf_exempt
def postbloguser(request):
	if request.method=='POST':
		title=request.POST.get('title')
		body=request.POST.get('body')
		image=request.FILES['image']
		b="BL00"
		x=1
		bid=b+str(x)
		while BlogData.objects.filter(Blog_ID=bid).exists():
			x=x+1
			bid=b+str(x)
		x=int(x)
		uid=request.session['userid']
		obj=BlogData(
			Blog_ID=bid,
			User_ID=uid,
			Title=title,
			Body=body,
			Image=image
			)
		obj.save()
		return redirect('/blog/')
@csrf_exempt
def changepassword(request):
	if request.method=='POST':
		old=request.POST.get('old')
		new=request.POST.get('new')
		obj=UserData.objects.filter(User_ID=request.session['userid'])
		alert=''
		password=''
		for x in obj:
			password=x.User_Password
			break
		if old==password:
			obj.update(
				User_Password=new,
			)
			return HttpResponse("<script>alert('Password Changed Successfully'); window.location.replace('/userdashboard/')</script>")
		else:
			return HttpResponse("<script>alert('Incorrect Password'); window.location.replace('/userdashboard/')</script>")

def addbusiness(request):
	try:
		uid=request.session['userid']
		if PlanSubscribeData.objects.filter(User_ID=uid, Plan_ID='PL001').exists():
			return HttpResponse("<script>alert('Please Upgrade Your Plan to Add More Business.'); window.location.replace('/userdashboard/')</script>")
		elif PlanSubscribeData.objects.filter(User_ID=uid, Plan_ID='PL002').exists():
			obj=BusinessData.objects.filter(User_ID=uid)
			businesscount=len(obj)
			if businesscount==3:
				return HttpResponse("<script>alert('Please Upgrade Your Plan to Add More Business.'); window.location.replace('/userdashboard/')</script>")
			else:
				obj=CategoryData.objects.all()
				dic={'data':obj,'checksession':checksession(request),}
				return render(request,'addbusiness3.html',dic)
		elif PlanSubscribeData.objects.filter(User_ID=uid, Plan_ID='PL003').exists():
			obj=CategoryData.objects.all()
			dic={'data':obj,'checksession':checksession(request),}
			return render(request,'addbusiness3.html',dic)
	except:
		obj=CategoryData.objects.all()
		dic={'data':obj,'checksession':checksession(request),}
		return render(request,'addbusiness1.html',dic)

def addbusiness3(request):
	obj=CategoryData.objects.all()
	dic={'data':obj,'checksession':checksession(request),}
	return render(request,'addbusiness3.html',dic)

@csrf_exempt
def savebusiness(request):
	if request.method=='POST':
		cname=request.POST.get('cname')
		cnumber=request.POST.get('cnumber')
		cemail=request.POST.get('cemail')
		bname=request.POST.get('bname')
		baddress=request.POST.get('baddress')
		bcity=request.POST.get('bcity')
		bstate=request.POST.get('bstate')
		bwebsite=request.POST.get('bwebsite')
		bdes=request.POST.get('bdes')
		bcategory=request.POST.get('bcategory')
		obj=BusinessData.objects.all().delete()
		b="B00"
		x=1
		bid=b+str(x)
		while BusinessData.objects.filter(Business_ID=bid).exists():
			x=x+1
			bid=b+str(x)
		x=int(x)
		obj=BusinessData(
			Business_ID=bid,
			User_ID=request.session['userid'],
			Contact_Name=cname,
			Contact_Number=cnumber,
			Contact_Email=cemail,
			Category_Name=bcategory,
			Business_Name=bname,
			Business_Address=baddress,
			Business_City=bcity,
			Business_State=bstate,
			Business_Website=bwebsite,
			Business_Decription=bdes
		)
		if BusinessData.objects.filter(Business_Name=bname).exists():
			return HttpResponse("<script>alert('Business Already Exists'); window.location.replace('/addbusiness3/')</script>")
		else:	
			obj.save()
			request.session['business_id'] = bid
			cid=''
			obj=CategoryData.objects.filter(Category_Name=bcategory)
			for x in obj:
				cid=x.Category_ID
			dic={'data':SubCategoryData.objects.filter(Category_ID=cid),'checksession':checksession(request),}
			return render(request,'addbusiness4.html',dic)
@csrf_exempt
def savebusiness2(request):
	if request.method=='POST':
		sname=request.POST.get('sname')
		logo=request.FILES['logo']
		obj=BusinessData.objects.filter(Business_ID=request.session['business_id'])
		obj.update(
			SubCategory_Name=sname
		)
		obj=BusinessLogoData(
			Business_ID=request.session['business_id'],
			Business_Logo=logo
			)
		obj.save()
		obj=BusinessData.objects.filter(Business_ID=request.session['business_id'])
		for x in obj:
			request.session['userid'] = x.User_ID
		return HttpResponse("<script>alert('Business Added Successfully'); window.location.replace('/userdashboard/')</script>")
	else:
		return redirect('/error404/')

def openbusinessdash(request, business):
	try:
		for x in BusinessData.objects.filter(Business_Name=business):
			request.session['businessid'] = x.Business_ID
		return redirect('/businessprofile/')
	except:
		return redirect('/error404/')
def openbusinessdash2(request):
	try:
		return redirect('/businessprofile/')
	except:
		return redirect('/error404/')

def addservice(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid']})
		return render(request,'business/addservice.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def saveservice(request):
	try:
		bid=request.session['businessid']
		if request.method=='POST':
			name=request.POST.get('name')
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
			)
			if ServicesData.objects.filter(Service_Name=name).exists():
				msg='Product/Service Already Exists'
				dic=GetBusinessData(bid)
				dic.update({'plan':request.session['planid'], 'msg':msg})
				return render(request,'business/addservice.html',dic)
			else:
				obj.save()
				msg='Product/Service Saved Successfully'
				dic=GetBusinessData(bid)
				dic.update({'plan':request.session['planid'], 'msg':msg})
				return render(request,'business/addservice.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def calllist(request):
	try:
		bid=request.session['businessid']
		obj=CallData.objects.filter(Business_ID=request.session['businessid'])
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid'],'data':reversed(obj)})
		return render(request,'business/userquries.html',dic)
	except:
		return redirect('/error404/')

def serviceslist(request):
	try:
		bid=request.session['businessid']
		obj=ServicesData.objects.filter(Business_ID=request.session['businessid'])
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid'],'data':obj})
		return render(request,'business/serviceslist.html',dic)
	except:
		return redirect('/error404/')
def deleteservice(request):
	try:
		bid=request.session['businessid']
		obj=ServicesData.objects.filter(Service_ID=request.GET.get('sid')).delete()
		obj=ServicesImagesData.objects.filter(Service_ID=request.GET.get('sid')).delete()
		obj=ServicesData.objects.filter(Business_ID=request.session['businessid'])
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid'],'data':obj})
		return render(request,'business/serviceslist.html',dic)
	except:
		return redirect('/error404/')
def changelogo(request):
	try:
		bid=request.session['businessid']
		obj=BusinessLogoData.objects.filter(Business_ID=bid)
		dic={}
		for x in obj:
			dic={'img':x.Business_Logo.url}
		dic.update(GetBusinessData(bid))
		dic.update({'plan':request.session['planid']})
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
def businesspostadbanner(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'banner':BusinessAdBannerData.objects.filter(Business_ID=bid)})
		dic.update({'plan':request.session['planid']})
		return render(request,'business/postadbanner.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def saverpostadbanner(request):
	if request.method=='POST':
		banner=request.FILES['banner']
		bid=request.session['businessid']
		uid=request.session['userid']
		plan=GetPlanID(uid)
		if plan=='PL002' and BusinessAdBannerData.objects.filter(Business_ID=bid).exists():
			return HttpResponse("<script>alert('Upgrade Your Plan to Post More'); window.location.replace('/postadbanner/')</script>")
		elif plan=='PL003':
			obj=BusinessAdBannerData.objects.filter(Business_ID=bid)
			bannercount=len(obj)
			if bannercount==2:
				return HttpResponse("<script>alert('Your are only allowed to add 2 Banners.'); window.location.replace('/postadbanner/')</script>")
			else:
				obj=BusinessAdBannerData(
					Business_ID=bid,
					Banner=banner
					)
				obj.save()
				return HttpResponse("<script>alert('Ad Banner Posted'); window.location.replace('/postadbanner/')</script>")
		else:
			obj=BusinessAdBannerData(
				Business_ID=bid,
				Banner=banner
			)
			obj.save()
			return HttpResponse("<script>alert('Ad Banner Posted'); window.location.replace('/postadbanner/')</script>")
def deletepostadbanner(request):
	banner=request.GET.get('banner')
	bid=request.session['businessid']
	obj=BusinessAdBannerData.objects.filter(Business_ID=bid, Banner=banner).delete()
	return redirect('/postadbanner/')

def businessreviews(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'reviews':BusinessReviewData.objects.filter(Business_ID=bid)})
		dic.update({'plan':request.session['planid']})
		return render(request,'business/reviews.html',dic)
	except:
		return redirect('/error404/')
def businessreviewreply(request):
	try:
		bid=request.session['businessid']
		obj=BusinessReviewReplyData(
			Review_ID=request.POST.get('rid'),
			Reply=request.POST.get('reply')
		)
		obj.save()
		review=''
		email=''
		for x in BusinessReviewData.objects.filter(Review_ID=request.POST.get('rid')):
			review=x.Review
			for y in UserData.objects.filter(User_ID=x.User_ID):
				email=y.User_Email
		sub='Addbiz4u Review Reply'
		msg='''Hi there!
Admin has replied on your review,

Review : '''+review+'''
Reply : '''+request.POST.get('reply')+'''

Thanks!
Team Addbiz4u'''
		email=EmailMessage(sub,msg,to=[email])
		email.send()
		return HttpResponse("<script>alert('Reply Sent!'); window.location.replace('/reviews/')</script>")
	except:
		return redirect('/error404/')

def businessmaplocation(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'map':BusinessMapsData.objects.filter(Business_ID=bid)})
		dic.update({'plan':request.session['planid']})
		return render(request,'business/maplocation.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def savemaplocation(request):
	if request.method=='POST':
		bid=request.session['businessid']
		maps=request.POST.get('maps')
		obj=BusinessMapsData.objects.filter(Business_ID=bid).delete()
		obj=BusinessMapsData(
			Business_ID=bid,
			Maps=maps
			)
		obj.save()
		return redirect('/maplocation/')
def businesssocialmedialinks(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'socialmedia':BusinessSocialMediaData.objects.filter(Business_ID=bid)})
		dic.update({'plan':request.session['planid']})
		return render(request,'business/socialmedialinks.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def savesocialmedialinks(request):
	if request.method=='POST':
		facebook=request.POST.get('facebook')
		instagram=request.POST.get('instagram')
		twitter=request.POST.get('twitter')
		obj=BusinessSocialMediaData.objects.filter(Business_ID=request.session['businessid']).delete()
		obj=BusinessSocialMediaData(
			Business_ID=request.session['businessid'],
			Facebook=facebook,
			Instagram=instagram,
			Twitter=twitter
			)
		obj.save()
		return redirect('/socialmedialinks/')
def businesseditbusinesshours(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid']})
		dic.update({'hours':BusinessData.objects.filter(Business_ID=bid)})
		return render(request,'business/editbusinesshours.html',dic)
	except:
		return redirect('/error404/')
@csrf_exempt
def savebusinesshours(request):
	if request.method=='POST':
		hour=request.POST.get('hours')
		bid=request.session['businessid']
		obj=BusinessData.objects.filter(Business_ID=bid)
		obj.update(Business_Hours=hour)
		return redirect('/editbusinesshours/')
@csrf_exempt
def savebusinessdays(request):
	if request.method=='POST':
		days=request.POST.get('days')
		bid=request.session['businessid']
		obj=BusinessData.objects.filter(Business_ID=bid)
		obj.update(Business_Days=days)
		return redirect('/editbusinesshours/')
def businesssettopbanner(request):
#	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid']})
		dic.update({'banner':BusinessTopBannerData.objects.filter(Business_ID=bid)})
		return render(request,'business/settopbanner.html',dic)
#	except:
#		return redirect('/error404/')
@csrf_exempt
def savetopbanner(request):
	if request.method=='POST':
		bid=request.session['businessid']
		banner=request.FILES['banner']
		obj=BusinessTopBannerData.objects.filter(Business_ID=bid)
		obj.delete()
		obj=BusinessTopBannerData(
			Business_ID=bid,
			Banner=banner)
		obj.save()
		return redirect('/settopbanner/')
def businessimagegallery(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		dic.update({'plan':request.session['planid']})
		dic.update({'image':BusinessImagesData.objects.filter(Business_ID=bid)})
		return render(request,'business/imagegallery.html',dic)
	except:
		return redirect('/error404/')

def deletebusinessimages(request):
	try:
		bid=request.session['businessid']
		image=request.GET.get('image')
		obj=BusinessImagesData.objects.filter(Business_ID=bid,
			Image=image).delete()
		return redirect('/imagegallery/')
	except:
		return redirect('/error404/')
@csrf_exempt
def savebusinessimages(request):
	if request.method=='POST':
		bid=request.session['businessid']
		image=request.FILES.getlist('image')
		for x in image:
			obj=BusinessImagesData(
				Business_ID=bid,
				Image=x
				)
			obj.save()
		return redirect('/imagegallery/')

def businessprofile(request):
	try:
		bid=request.session['businessid']
		dic=GetBusinessData(bid)
		plan=request.session['planid']
		dic.update({'plan':plan})
		request.session['planid'] = plan
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
		del request.session['userid']
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
		if e=='admin@addbiz4u.com' and p=='1234':
			request.session['adminid'] = 'admin@addbiz4u.com'
			return render(request,'adminpages/index.html',{})
		else:
			return HttpResponse("<script>alert('Incorrect Credentials.'); window.location.replace('/adminlogin/')</script>")

def addcategory(request):
	try:
		adminid=request.session['adminid']
		return render(request,'adminpages/addcategory.html',{})
	except:
		return redirect('/error404/')
@csrf_exempt
def savecategory(request):
	if request.method=='POST':
		category=request.POST.get('category')
		image=request.FILES['image']
		c="CA00"
		x=1
		cid=c+str(x)
		while CategoryData.objects.filter(Category_ID=cid).exists():
			x=x+1
			cid=c+str(x)
		x=int(x)
		obj=CategoryData(
			Category_ID=cid,
			Category_Name=category,
			Category_Image=image
			)
		obj.save()
		return render(request,'adminpages/addcategory.html',{'msg':'Saved Successfully'})
	else:
		return redirect('/error404/')
def defaultcategorieslist(request):
	try:
		adminid=request.session['adminid']
		dic={'data':CategoryData.objects.all()}
		return render(request,'adminpages/defaultcategorieslist.html',dic)
	except:
		return redirect('/error404/')
def deletecategory(request):
	try:
		adminid=request.session['adminid']
		obj=CategoryData.objects.filter(Category_ID=request.GET.get('cid')).delete()
		return redirect('/defaultcategorieslist/')
	except:
		return redirect('/error404/')

def addsubcategory(request):
	try:
		adminid=request.session['adminid']
		dic={'data':CategoryData.objects.all()}
		return render(request,'adminpages/addsubcategory.html',dic)
	except:
		return redirect('/error404/')

@csrf_exempt
def savesubcategory(request):
	if request.method=='POST':
		category=request.POST.get('category')
		subcategory=request.POST.get('subcategory')
		subcategoryimage=request.FILES['subcategoryimage']
		s="SC00"
		x=1
		sid=s+str(x)
		while SubCategoryData.objects.filter(SubCategory_ID=sid).exists():
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
@csrf_exempt
def postreq(request):
	if request.method=='POST':
		bid=request.POST.get('bid')
		uid=request.session['userid']
		title=request.POST.get('title')
		des=request.POST.get('des')
		c="P00"
		x=1
		cid=c+str(x)
		while PostData.objects.filter(Post_ID=cid).exists():
			x=x+1
			cid=c+str(x)
		x=int(x)
		obj=PostData(
			Post_ID=cid,
			Business_ID=bid,
			User_ID=uid,
			Post_Title=title,
			Post_Description=des
		)
		obj.save()
		return HttpResponse("<script>alert('Posted Successfully'); window.location.replace('/userdashboard/')</script>")

def leads(request):
	lt=GetLeads()
	page = request.GET.get('page')
	paginator = Paginator(list(reversed(lt)), 10)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	dic={'data':data,
		'checksession':checksession(request),
		'lead1':GetLeads(),
		'lead':UserLeadsData.objects.filter(User_ID=request.session['userid'])}
	return render(request,'leads.html',dic)
def getlead(request):
	try:
		uid=request.session['userid']
		pid=request.GET.get('pid')
		obj=UserLeadsData(
			User_ID=uid,
			Post_ID=pid
			)
		obj.save()
		bdata={}
		pdata=''
		for x in PostData.objects.filter(Post_ID=pid):
			bdata=GetBusinessData(x.Business_ID)
			pdata=x.Post_Description
		sub='Biz4u - Lead Information'
		msg='''Hi there!
New Lead has been added to My Leads section of your profile,

Contact Name : '''+bdata['owner']+'''
Mobile : '''+bdata['mobile']+'''
Email : '''+bdata['email']+'''
Address : '''+bdata['address']+'''
City : '''+bdata['city']+'''
State : '''+bdata['state']+'''
Business Name : '''+bdata['name']+'''
Post : '''+pdata+'''

Thanks!
Team Biz4u'''
		umail=''
		for x in UserData.objects.filter(User_ID=uid):
			umail=x.User_Email
		email=EmailMessage(sub,msg,to=[bdata['email'],umail])
		email.send()
		return HttpResponse("<script>alert('Lead has been added to Your Leads List'); window.location.replace('/leads/')</script>")
	except:
		return redirect('/error404/')

def requestlead(request):
	try:
		uid=request.session['userid']
		pid=request.GET.get('pid')
		bdata={}
		pdata=''
		for x in PostData.objects.filter(Post_ID=pid):
			bdata=GetBusinessData(x.Business_ID)
			pdata=x.Post_Description
		sub='Biz4u - Lead Information'
		msg='''Hi there!
New Lead has been added to My Leads section of your profile,

Contact Name : '''+bdata['owner']+'''
Mobile : '''+bdata['mobile']+'''
Email : '''+bdata['email']+'''
Address : '''+bdata['address']+'''
City : '''+bdata['city']+'''
State : '''+bdata['state']+'''
Business Name : '''+bdata['name']+'''
Post : '''+pdata+'''

Thanks!
Team Biz4u'''
		umail=''
		for x in UserData.objects.filter(User_ID=uid):
			umail=x.User_Email
		email=EmailMessage(sub,msg,to=[bdata['email'],umail])
		email.send()
		return HttpResponse("<script>alert('Lead Sent'); window.location.replace('/leads/')</script>")
	except:
		return redirect('/error404/')
@csrf_exempt
def getcall(request):
	if request.method=='POST':
		bid=request.POST.get('bid')
		name=request.POST.get('name')
		number=request.POST.get('number')
		message=request.POST.get('message')
		dic=GetBusinessData(bid)
		c="CLL00"
		x=1
		cid=c+str(x)
		while CallData.objects.filter(Call_ID=cid).exists():
			x=x+1
			cid=c+str(x)
		x=int(x)
		obj=CallData(
			Call_ID=cid,
			Business_ID=bid,
			Customer_Name=name,
			Customer_Number=number,
			Customer_Message=message
			)
		obj.save()
		sub='Biz4u - Query for Your Business'
		msg='''Hi there!
You got a query message for your business'''+dic["name"]+''' from,

Name : '''+name+'''
Mobile : '''+number+'''
Message : '''+message+'''

Thanks!
Team Biz4u'''
		email=EmailMessage(sub,msg,to=[dic['email']])
		email.send()
		return HttpResponse("<script>alert('Query Sent! You will got a call soon!'); window.location.replace('/index/')</script>")
def pricing(request):
	dic={'checksession':checksession(request)}
	return render(request,'pricing.html',dic)
def upgradeaccount(request):
	planid=request.GET.get('planid')
	uid=request.session['userid']
	if planid=='PL001':
		if PlanSubscribeData.objects.filter(Plan_ID='PL001',User_ID=uid).exists():
			return HttpResponse("<script>alert('You have already subscribed to this plan.'); window.location.replace('/userdashboard/')</script>")
		else:
			obj=PlanSubscribeData.objects.filter(User_ID=uid).delete()
			obj=PlanSubscribeData(
				Plan_ID='PL001',
				User_ID=request.session['userid']
				)
			obj.save()
			return HttpResponse("<script>alert('Congratulation! You have Successfully subscribed to our Free Plan.'); window.location.replace('/userdashboard/')</script>")
	if planid=='PL002':
		if PlanSubscribeData.objects.filter(Plan_ID='PL002',User_ID=uid).exists():
			return HttpResponse("<script>alert('You have already subscribed to this plan.'); window.location.replace('/userdashboard/')</script>")
		else:
			obj=PlanSubscribeData.objects.filter(User_ID=uid).delete()
			p="PAY00"
			x=1
			pid=p+str(x)
			while PaymentData.objects.filter(Pay_ID=pid).exists():
				x=x+1
				pid=p+str(x)
			x=int(x)
			obj=PaymentData(
				Pay_ID=pid,
				Plan_ID=planid,
				User_ID=request.session['userid']
				)
			obj.save()
			return redirect('/checkout/?payid='+pid+'&planid='+planid)
	if planid=='PL003':
		if PlanSubscribeData.objects.filter(Plan_ID='PL003',User_ID=uid).exists():
			return HttpResponse("<script>alert('You have already subscribed to this plan.'); window.location.replace('/userdashboard/')</script>")
		else:
			obj=PlanSubscribeData.objects.filter(User_ID=uid).delete()
			p="PAY00"
			x=1
			pid=p+str(x)
			while PaymentData.objects.filter(Pay_ID=pid).exists():
				x=x+1
				pid=p+str(x)
			x=int(x)
			obj=PaymentData(
				Pay_ID=pid,
				Plan_ID=planid,
				User_ID=request.session['userid']
				)
			obj.save()
			return redirect('/checkout/?payid='+pid+'&planid='+planid)
import app.Checksum as Checksum
def checkout(request):
	uid=request.session['userid']
	payid=request.GET.get('payid')
	planid=request.GET.get('planid')
	amount=0
	if planid=='PL002':
		amount=999
	elif planid=='PL003':
		amount=1499
	dic={
	'ORDER_ID':payid,
	'TXN_AMOUNT':str(amount),
	'CUST_ID':uid,
	'INDUSTRY_TYPE_ID':'Retail',
	'WEBSITE':'None',
	'CHANNEL_ID':'WEB',
	'WEBSITE':'WEBSTAGING',
	'CALLBACK_URL':'http://127.0.0.1:8000/verifypayment/'
	}
	print(dic)
	MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
	MID = 'bAQrse69179758299775'
	data_dict = {'MID':MID}
	data_dict.update(dic)
	param_dict = data_dict
	param_dict['CHECKSUMHASH'] =Checksum.generateSignature(data_dict, MERCHANT_KEY)
	obj=UserData.objects.filter(User_ID=uid)
	param_dict.update({'userdata':obj,'planamount':amount,'planid':planid})
	return render(request,'checkout.html',param_dict)

import cgi
@csrf_exempt
def verifypayment(request):
		MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
		MID = 'bAQrse69179758299775'
		CURRENCY=request.POST.get('CURRENCY')
		GATEWAYNAME=request.POST.get('GATEWAYNAME')
		RESPMSG=request.POST.get('RESPMSG')
		BANKNAME=request.POST.get('BANKNAME')
		PAYMENTMODE=request.POST.get('PAYMENTMODE')
		RESPCODE=request.POST.get('RESPCODE')
		TXNID=request.POST.get('TXNID')
		TXNAMOUNT=request.POST.get('TXNAMOUNT')
		ORDERID=request.POST.get('ORDERID')
		STATUS=request.POST.get('STATUS')
		BANKTXNID=request.POST.get('BANKTXNID')
		TXNDATE=request.POST.get('TXNDATE')
		CHECKSUMHASH=request.POST.get('CHECKSUMHASH')
		respons_dict = {
						'MERCHANT_KEY':MERCHANT_KEY,
						'CURRENCY':CURRENCY,
						'GATEWAYNAME':GATEWAYNAME,
						'RESPMSG':RESPMSG,
						'BANKNAME':BANKNAME,
						'PAYMENTMODE':PAYMENTMODE,
						'MID':MID,
						'RESPCODE':RESPCODE,
						'TXNID':TXNID,
						'TXNAMOUNT':TXNAMOUNT,
						'ORDERID':ORDERID,
						'STATUS':STATUS,
						'BANKTXNID':BANKTXNID,
						'TXNDATE':TXNDATE,
						'CHECKSUMHASH':CHECKSUMHASH
		}
		checksum=respons_dict['CHECKSUMHASH']
		if 'GATEWAYNAME' in respons_dict:
			if respons_dict['GATEWAYNAME'] == 'WALLET':
				respons_dict['BANKNAME'] = 'null';
		obj=PaymentData2(
			Pay_ID=ORDERID,
			CURRENCY=CURRENCY,
			GATEWAYNAME=str(GATEWAYNAME),
			RESPMSG=RESPMSG,
			BANKNAME=str(BANKNAME),
			PAYMENTMODE=str(PAYMENTMODE),
			RESPCODE=RESPCODE,
			TXNID=str(TXNID),
			TXNAMOUNT=TXNAMOUNT,
			STATUS=STATUS,
			BANKTXNID=BANKTXNID,
			TXNDATE=str(TXNDATE),
			CHECKSUMHASH=CHECKSUMHASH
			)
		obj.save()
		custid=''
		obj=PaymentData.objects.filter(Pay_ID=ORDERID)
		for x in obj:
			custid=x.User_ID
		data_dict = {
			'MID':respons_dict['MID'],
			'ORDER_ID':ORDERID,
			'TXN_AMOUNT':TXNAMOUNT,
			'CUST_ID':custid,
			'INDUSTRY_TYPE_ID':'Retail',
			'WEBSITE':'None',
			'CHANNEL_ID':'WEB',
			'WEBSITE':'WEBSTAGING',
			'CALLBACK_URL':'http://127.0.0.1:8000/verifypayment/'
			}
		checksum =Checksum.generateSignature(data_dict, MERCHANT_KEY)
		
		verify = Checksum.verifySignature(data_dict, MERCHANT_KEY, checksum)
		if verify:
			if respons_dict['RESPCODE'] == '01':
				userid=''
				planid=''
				obj=PaymentData.objects.filter(Pay_ID=ORDERID)
				for x in obj:
					userid=x.User_ID
					planid=x.Plan_ID
				obj=PlanSubscribeData(
					Plan_ID=planid,
					User_ID=userid
					)
				obj.save()
				return HttpResponse("<script>alert('Account has been upgraded successfully!'); window.location.replace('/userdashboard/')</script>")
			else:
				return HttpResponse("<script>alert('Account has been upgradation Failed!'); window.location.replace('/userdashboard/')</script>")
		else:
			return HttpResponse("<script>alert('Account has been upgradation Failed!'); window.location.replace('/userdashboard/')</script>")
	
def freeads(request):
	return render(request,'freeads.html',{})
def about(request):
	return render(request,'about.html',{})
def classifiedads(request):
	return render(request,'classifiedads.html',{})
def classifieddetail(request):
	return render(request,'classifieddetail.html',{})
def adminuserslist(request):
	return render(request,'adminpages/userslist.html',{})
def admindeactiveusers(request):
	return render(request,'adminpages/deactiveusers.html',{})
def adminplanssubscriptions(request):
	return render(request,'adminpages/planssubscriptions.html',{})
def adminplanpayments(request):
	return render(request,'adminpages/planpayments.html',{})
def adminbusinesslists(request):
	return render(request,'adminpages/businesslists.html',{})
def adminbusinessleads(request):
	return render(request,'adminpages/businessleads.html',{})
def adminpostblog(request):
	return render(request,'adminpages/postblog.html',{})
def adminbloglist(request):
	return render(request,'adminpages/bloglist.html',{})
def adminadsforsell(request):
	return render(request,'adminpages/adsforsell.html',{})
def adminadsforrent(request):
	return render(request,'adminpages/adsforrent.html',{})
