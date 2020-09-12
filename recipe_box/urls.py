"""recipe_box URL Configuration

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

from recipe_app import views

urlpatterns = [
    path('', views.main_view, name="homepage"),
    path('recipe/<int:recipe_id>/edit', views.recipe_edit_view),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('authors/<int:author_id>/', views.author_detail),
    path('addrecipe/', views.add_recipe, name="addrecipe"),
    path('addauthor/', views.add_author, name="addauthor"),
    path('favorite/<int:pk>/', views.favorite, name='favorite'),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('signup/', views.signup_view, name="signupview"),
    path('admin/', admin.site.urls),
]
