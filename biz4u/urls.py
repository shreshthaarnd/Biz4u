"""biz4u URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog),
    path('cart/',cart),
    path('category/',category),
    path('checkout/',checkout),
    path('confirmation/',confirmation),
    path('contact/',contact),
    path('elements/',elements),
    path('index/',index),
    path('login/',login),
    path('registration/',registration),
    path('singleblog/',singleblog),
    path('singleproduct/',singleproduct),
    path('tracking/',tracking),
    path('navbar/',adminnavbar),
    path('adminindex/',adminindex),
    path('sidebar/',adminsidebar),
    path('basicelements/',adminbasicelements),
    path('basictable/',adminbasictable),
    path('blankpage/',adminblankpage),
    path('buttons/',adminbuttons),
    path('chartjs/',adminchartjs),
    path('dropdowns/',admindropdowns),
    path('error404/',adminerror404),
    path('error500/',adminerror500),
    path('fontawesome/',adminfontawesome),
    path('adminlogin/',adminlogin),
    path('adminregister/',adminregister),
    path('typography/',admintypography),
    path('adminlogincheck/',adminlogincheck),
    path('defaultcategorieslist/',defaultcategorieslist),
    path('addsubcategory/',addsubcategory),
]
