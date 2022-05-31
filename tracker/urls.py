from django.urls import path
from . import views
urlpatterns = [
    path('world/',views.world,name="world"),
    path('',views.india,name="india"),
    path('know-covid19/',views.home,name="home"),
    path('helpline/',views.helpline,name="helpline"),
    path('donate/',views.donate,name="donate"),
]
