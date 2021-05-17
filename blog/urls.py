from . import views
from django.urls import path ,include




app_name='blog'

urlpatterns = [
    path('',views.PostListView.as_view() ,name='blog-list'),
    path('create',views.PostCreateView.as_view() ,name='blog-create'),
    path('<int:pk>/',views.PostDetailView.as_view() ,name='blog-single'),
    path('<int:pk>/update/',views.PostUpdateView.as_view() ,name='blog-update'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view() ,name='blog-delete'),

]
