from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='shop'),
    path('login_p/', views.login_p,name='login_p'),
    path('about/', views.about,name='about'),
    path('signup/', views.signup,name='signup'),
    path('addcourse/', views.addcourse,name='addcourse'),
    path('mycoursess/', views.mycoursess,name='mycoursess'),
    path('logout_p/', views.logout_p,name='logout_p'),
    path('profile_p/', views.profile_p,name='profile_p'),
    path('contact/', views.contact, name='contact')

]
