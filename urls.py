from django.urls import path

import views

# urls for website 
urlpatterns = [
    path('', views.index),
    path('blog', views.blog),
    path('projects', views.projects),
    path('about', views.about),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

