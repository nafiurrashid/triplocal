from django.urls import path #import path from project urls.py
from . import views  #import views from all 


urlpatterns =[
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),

 
]
#mutiple urls to mapping will be withing this array
#IN views.home home means there will be a home function