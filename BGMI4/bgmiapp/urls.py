from bgmiapp.models import withdraw
from django.contrib import admin
from django.urls import path
from . import views
from .views import ShowProfilePageView,UpdateProfilePageView,ShowBalanceView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',views.homeview,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('showprofile/',ShowProfilePageView.as_view(),name='show_profile'),
    path('updateprofile/',UpdateProfilePageView.as_view(),name='update_profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bgmiapp/logout.html'),name='logout'),
    path('solo/',views.solo,name="solo"),
    path('duo/',views.duo,name='duo'),
    path('squad/',views.squad,name='squad'),
    path('result/',views.Result,name="result"),
    path('solomatchresult/',views.Solomatchresult,name='solomatchresult'),
    path('showbalance/',ShowBalanceView.as_view(),name="showbalance"),
    path('withdraw/',views.WithdrawView,name="withdraw")

]