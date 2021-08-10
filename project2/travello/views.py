from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Destination 
from django.contrib import messages
from django.core.paginator import Paginator




# Create your views here.
def index(request):
    
    # dest1 = Destination() 
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City That Never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer= False
   

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'First Biryani, Then Sherwani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer= True

    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.desc = 'Beautiful City'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 750
    # dest3.offer= False



    # dests = [dest1, dest2, dest3]
    if 'q' in request.GET:
       
        q=request.GET['q']
        posts=Destination.objects.filter(title_icontains=q)
         
    else:
        posts=Destination.objects.all()
   #pagination
    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)


    dests=Destination.objects.all()
    return render(request, "index.html", context={'dests': dests,'posts':posts_obj})
    # return render(request, "index.html", {'dests': dests})





def about(request):
    return render(request,"about.html")    
def news(request):
    return render(request,"news.html")
def contact(request):
    return render(request,"contact.html") 
