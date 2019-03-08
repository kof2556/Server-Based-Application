import requests
from django.http import HttpResponse
from django.shortcuts import render
#Functions for pages
def index(request):
    content_html = open("content/index.html").read()
    ontext = {
       "content": content_html,
    }
    return render(request, 'base.html', context)
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/blog">Blog</a> <br />
        <a href="/projects">Projects</a> <br />
        <a href="/about">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')
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

#virtual site is working, make sure to add navigations onto the other pages and see about css 


