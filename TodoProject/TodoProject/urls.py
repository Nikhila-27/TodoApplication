"""
URL configuration for TodoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.UserRegisterView.as_view(),name="user_register"),
    path('',views.UserLoginView.as_view(),name="user_login"),
    path('logout',views.LogoutView.as_view(),name="user_logout"),
    path('home',views.Home.as_view(),name="home_view"),
    path('create',views.TodoCraeteView.as_view(),name="create_view"),
    path('delete/<int:id>',views.TodoDeleteView.as_view(),name="delete_view"),
    path('update/<int:id>',views.TodoUpdateView.as_view(),name="update_view"),
    
    

]
