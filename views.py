import requests
from django.http import HttpResponse
from django.shortcuts import render
#Functions for pages
def index(request):
    content_html = open("content/index.html").read()
    context = {
       "content": content_html,
       
    }
    return render(request, 'base.html', context)
    
#blog page
def blog(request):
    content_html = open("content/blog.html").read()
    context = {
       "content": content_html,
    }
    return render(request, 'base.html', context)
#projects page    
def projects(request):
    content_html = open("content/projects.html").read()
    context = {
        "content": content_html,
    }
    return render(request, 'base.html', context)
#about me page
def about(request):
    content_html = open("content/about.html").read()
    context = {
        "content": content_html,
    }
    return render(request, 'base.html', context)


def github_api_example(request):
    # We can also combine Django with APIs, or 
    response = requests.get('https://github.com/kof2556/Server-Based-Application')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)


