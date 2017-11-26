"""crowdbotics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from main import views as core_views


urlpatterns = [
    url(r'^api/v1/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^$', core_views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^dogs/$', login_required(core_views.DogList.as_view()), name='dog-list'),
    url(r'^dogs/add$', login_required(core_views.DogCreate.as_view()), name='dog-add'),

    url(r'^cats/$', login_required(core_views.CatList.as_view()), name='cat-list'),
    url(r'^cats/add$', login_required(core_views.CatCreate.as_view()), name='cat-add'),
]
