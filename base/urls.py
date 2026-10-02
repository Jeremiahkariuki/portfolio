from django.urls import path
from django.views.generic.base import RedirectView
from django.templatetags.static import static
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('projects/', views.projects, name='projects'),
    path('favicon.ico', RedirectView.as_view(url=static('base/images/image1.jpeg'))),
]