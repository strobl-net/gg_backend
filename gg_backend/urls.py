"""gg_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from accounts.views import RegisterAPI, LoginAPI, UserAPI
from surveys.views import SurveyView
from answers.views import AnswerView
from accounts.views import ProfileView

router = routers.DefaultRouter()
router.register('api/surveys', SurveyView)
router.register('api/answers', AnswerView)
router.register('api/profiles', ProfileView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterAPI.as_view()),
    path('api/auth/login/', LoginAPI.as_view()),
    path('api/auth/user/', UserAPI.as_view()),
    path('api/auth/', include('knox.urls')),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('', include(router.urls))
]
