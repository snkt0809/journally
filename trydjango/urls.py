"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import home_view
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
from articles.views import (
    article_search_view,
    article_create_view,
    article_detail_view,
)

urlpatterns = [ 
    path('', home_view),  # This is the URL for the home view
    path('articles/', article_search_view),  # This is the URL for the articles app
    path('articles/create/', article_create_view),  # This is the URL for the articles app
    path('articles/<int:id>/', article_detail_view),  # This is the URL for the articles app
    path('admin/', admin.site.urls),
    path('login/', login_view),  # This is the URL for the login view
    path('logout/', logout_view),  # This is the URL for the logout view
    path('register/', register_view),  # This is the URL for the register view
]
