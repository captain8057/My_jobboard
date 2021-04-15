from . import views
from django.contrib import admin
from django.urls import path ,include



app_name='accounts'

urlpatterns = [
    path('logout',views.logoutUser ,name='logout'),
    path('signup',views.signup ,name='signup'),
    path('profile',views.Profile ,name='profile'),
    path('login',views.login ,name='login'),
    path('profile/edit',views.profile_edit ,name='profile_edit'),


]
