from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('',index),
    path('login/',login),
    path('forgotpassword/',forgotpassword),
    path('sendpassword/',sendpassword),
    path('registration/',registration),
    path('singleblog/',singleblog),
    path('singleproduct/',singleproduct),
    path('opencity/',opencity),
    path('tracking/',tracking),
    path('savebusiness/',savebusiness),
    path('savebusiness2/',savebusiness2),
    path('logincheck/',logincheck),
    path('addservice/',addservice),
    path('saveservice/',saveservice),
    path('servicelist/',serviceslist),
    path('deleteservice/',deleteservice),
    path('changelogo/',changelogo),
    path('savelogo/',savelogo),
    path('businessprofile/',businessprofile),
    path('editbusinessdetails/',editbusinessdetails),
    path('logout/',logout),
    path('saveuser/',saveuser),
    path('saveuser2/',saveuser2),
    path('verifyaccount/',verifyaccount),
    path('resendOTP/',resendOTP),
    path('addbusiness/',addbusiness),
    path('addbusiness3/',addbusiness3),
    path('leads/',leads),
    path('pricing/',pricing),
    path('freeads/',freeads),
    path('about/',about),
    path('classifieddetail/',classifieddetail),
    path('adminuserslist/',adminuserslist),
    path('admindeactiveusers/',admindeactiveusers),
    path('adminplanssubscriptions/',adminplanssubscriptions),
    path('adminplanpayments/',adminplanpayments),
    path('adminbusinesslists/',adminbusinesslists),
    path('adminbusinessleads/',adminbusinessleads),
    path('adminpostblog/',adminpostblog),
    path('adminsaveblog/',adminsaveblog),
    path('adminbloglist/',adminbloglist),
    path('adminadsforsell/',adminadsforsell),
    path('adminadsforrent/',adminadsforrent),
    path('makeuseractive/',makeuseractive),
    path('makeuserdeactive/',makeuserdeactive),
    path('adminadsforbuy/',adminadsforbuy),
    path('deletead/',admindeletead),
    path('admindeleteblog/',admindeleteblog),
    path('adminlogout/',adminlogout),
    path('savenewsletter/',savenewsletter),
    path('sendcontactform/',sendcontactform),
    path('downloaddatabase/',downloaddatabase),

    path('searchresult/',searchresult),
    path('privacypolicy/',privacypolicy),
    path('termsconditions/',termsconditions),
    path('disclaimer/',disclaimer),
    path('faq/',faq),
    path('featured/',featuredlisting),

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
    path('postadd/',postadd),
    path('classifieds/',classifieds),
    path('savead/',savead),
    path('sellads/',sellads),
    path('rentads/',rentads),
    path('addcategory/',addcategory),
    path('savecategory/',savecategory),
    path('deletecategory/',deletecategory),
    path('savesubcategory/',savesubcategory),
    path('subcategorylist/',subcategorylist),
    path('deletesubcategory/',deletesubcategory),
    path('openbusinessdash/',openbusinessdash2),
    path('<str:business>/openbusinessdash/',openbusinessdash),
    path('userdashboard/',userdashboard),
    path('edituserdata/',edituserdata),
    path('changepassword/',changepassword),
    path('getcall/',getcall),
    path('calllist/',calllist),
    path('postreq/',postreq),
    path('leads/',leads),
    path('getlead/',getlead),
    path('requestlead/',requestlead),
    path('postadbanner/',businesspostadbanner),
    path('saverpostadbanner/',saverpostadbanner),
    path('deletepostadbanner/',deletepostadbanner),
    path('maplocation/',businessmaplocation),
    path('savemaplocation/',savemaplocation),
    path('socialmedialinks/',businesssocialmedialinks),
    path('savesocialmedialinks/',savesocialmedialinks),
    path('editbusinesshours/',businesseditbusinesshours),
    path('savebusinesshours/',savebusinesshours),
    path('savebusinessdays/',savebusinessdays),
    path('settopbanner/',businesssettopbanner),
    path('savetopbanner/',savetopbanner),
    path('imagegallery/',businessimagegallery),
    path('savebusinessimages/',savebusinessimages),
    path('deletebusinessimages/',deletebusinessimages),
    path('reviews/',businessreviews),
    path('savereview/',savereview),
    path('replyreview/',businessreviewreply),
    path('saveplan/',saveplan),
    path('upgradeaccount/',upgradeaccount),
    path('verifypayment/',verifypayment),
    path('postbloguser/',postbloguser),
    path('classifiedscategories/',classifiedsCategories),
    path('adminsendmails/',adminsendmails),
    path('editcategory/',editcategory),
    path('admindeletebusiness/',admindeletebusiness),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
