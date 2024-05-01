from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about , name='about'),
    path('online', views.online, name='online'),
    path('contact', views.contact , name='contact'),
    path('course', views.course , name='course'),
    path('index', views.index , name='index'),

]