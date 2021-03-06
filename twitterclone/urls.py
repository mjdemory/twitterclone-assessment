"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from twitteruser import views
from authentication.views import login_view, logout_view
from tweet.views import create_tweet_view, tweet_detail_view
from notification.views import notification_view

urlpatterns = [
    path('', views.index, name='homepage'),
    path('create_tweet_view/', create_tweet_view, name='createtweet'),
    path('tweet_detail_view/<int:tweet_id>/', tweet_detail_view, name='tweetdetail'),
    path('user_detail_view/<int:tweet_id>/', views.user_detail_view, name='userdetail'),
    path('notification_view/', notification_view, name='notification'),
    path('login_view/', login_view, name='login'),
    path('signup_view/', views.signup_view),
    path('logout_view/', logout_view, name='logout'),
    path('follow_view/<int:follow_id>/', views.follow_view, name='follow_view'),
    path('unfollow_view/<int:unfollow_id>/', views.unfollow_view, name='unfollow_view'),
    path('admin/', admin.site.urls),
    
]
