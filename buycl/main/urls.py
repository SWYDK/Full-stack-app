
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import ClothesView
urlpatterns = [
    path('home',views.home,name="home"),



    

]
