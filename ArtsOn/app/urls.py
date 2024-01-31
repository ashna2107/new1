"""
URL configuration for ArtsOn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about',views.about1),
    path('gallery',views.gallery),
    path('login',views.login),
    path('contact',views.contact),
    path('conhome',views.conhome),
    path('user',views.user),
    path('danceteam',views.danceteam),
    path('music',views.music),
    path('admindance',views.admindance),
    path('adminuser',views.adminuser),
    path('adminhome',views.adminhome),
    path('adminmusic',views.adminmusic),
    path('ser',views.ser),
    path('delete/<id1>',views.delete),
    path('delete1/<id1>',views.delete1),
    path('services',views.services),
    path('paid',views.paid),
    path('paid1',views.paid1),
    path('profile',views.profile1),
    path('profile2',views.profile2),
    path('uprofile',views.uprofile),
    path('edituser/<id2>',views.edituser),
    path('dancepage',views.dancepage),
    path('pending',views.pending),
    path('logout',views.logout),
    path('addprojects',views.addprojects),
    path('caddprojects',views.caddprojects),
    path('pending1/<id1>',views.pending1),
    path('pending01',views.pending01),
    path('pending02/<id2>',views.pending02),
    path('edititem/<id3>',views.edititem),
    path('edititem1/<id5>',views.edititem1),
    path('viewdetails/<dp>',views.viewdetails),
    path('cprofile/<dp>',views.cprofile),
    path('display',views.display),
    path('mabout',views.mabout),
    path('dabout',views.dabout),
    path('booking/<bok>',views.boooking),
    path('booking1/<bok>',views.boooking1),
    path('bookings/<bk>',views.bookings),
    path('editdm/<dd>',views.editdm),
    path('editdd/<dk>',views.editdd),
    path('mbook',views.mbook),
    path('mbook1',views.mbook1),
    path('book',views.book),
    path('book1',views.book1),
    path('accept/<k>',views.accept),
    path('daccept/<k>',views.daccept),
    path('reject/<bk>',views.reject),
    path('dreject/<bk>',views.dreject),
    path('payment/<a>/<bid>',views.payment),
    path('success',views.success),
    path('addreviews',views.addreviews),

]
