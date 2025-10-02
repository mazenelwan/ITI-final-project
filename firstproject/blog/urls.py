from django.urls import path
from . import views

urlpatterns = [ 
  path('', views.home, name=''),
  path('shop', views.shop2, name='shop'),
  path('contact', views.contact, name='contact'),
  path('about', views.about, name='about'),
 ]