from . import views
from django.contrib import admin
from django.urls import path ,include



app_name='job'

urlpatterns = [
    path('',views.job_list ,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<int:id>',views.job_detail,name='job_detailurl'),
    # path('user/favourites',views.user_favourites , name='user_favourites'),
    path('<int:id>/like_or_dislike',views.like_or_unlike , name='like'),

]
