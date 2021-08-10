from django.urls import path #import path from project urls.py
from . import views #import views from all 

urlpatterns =[
    path('',views.home, name='home'),
    path('add',views.add, name='add')
]
#mutiple urls to mapping will be withing this array
#IN views.home home means there will be a home function