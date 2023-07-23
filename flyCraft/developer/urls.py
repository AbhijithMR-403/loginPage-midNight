from django.urls import path
from developer import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('register/',views.register,'register'),
    # path('about',views.about,name='about'),
    # path('contact',views.contact,name='contact'),
    # path('blog',views.blog,name='blog'),
    # path('services',views.services,name='services'),
    # path('login',views.handlelogin,name='handlelogin'),
    # path('logout',views.handlelogout,name='handlelogout'),
    # path('signup',views.handlesignup,name='handlesignup'),
    

]
