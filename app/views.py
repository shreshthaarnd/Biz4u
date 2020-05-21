from django.shortcuts import render

# Create your views here.
def blog(request):
	return render(request,'blog.html',{})
def cart(request):
	return render(request,'cart.html',{})
def category(request):
	return render(request,'category.html',{})
def checkout(request):
	return render(request,'checkout.html',{})
def contact(request):
	return render(request,'contact.html',{})
def confirmation(request):
	return render(request,'confirmation.html',{})
def elements(request):
	return render(request,'elements.html',{})
def index(request):
	return render(request,'index.html',{})
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

