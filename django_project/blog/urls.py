from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
    #path('restaurant/', views.restaurants, name='blog-restaurants'),
    path('restaurant/', PostListView.as_view(), name='blog-restaurants'),
    path('restaurantdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),


]

