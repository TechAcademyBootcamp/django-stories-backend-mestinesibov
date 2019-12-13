from django.shortcuts import render

# Create your views here.

def home_function(request):
    return render(request,'index.html')

def about_function(request):
    return render(request,'about.html')

def contact_function(request):
    return render(request,'contact.html')

def create_story_function(request):
    return render(request,'create_story.html')  

def email_function(request):
    return render(request,'email-subscribes.html') 

def recipes_function(request):
    return render(request,'recipes.html')

def single_function(request):
    return render(request,'single.html') 

def stories_function(request):
    return render(request,'stories.html')

def userp_function(request):
    return render(request,'user-profile.html')