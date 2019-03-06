import requests
from django.http import HttpResponse
from django.shortcuts import render
#Functions for pages
def index(request):
  
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/blog">Blog</a> <br />
        <a href="/projects">Projects</a> <br />
        <a href="/about">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')
#blog page
def blog(request):
   
    context = {
       
    }
    return render(request, 'blog.html', context)
#projects page    
 def projects(request):
   
    context = {
       
    }
    return render(request, 'projects.html', context)
#about me page
def about(request):
  
    context = {
        
    }
    return render(request, 'about.html', context)



