"""Healthy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


from django.urls import path,include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name="Index"),
    path('about/',AboutView.as_view(), name="About"),

    ## AUTH 
    path('login/',ChildLoginView.as_view(),name="Child Login"),
    path('register/', ChildRegisterView.as_view(), name="Child Registration"),
    url(r'^activate/(?P<b64id>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate,name="Activate"),

    path('caretaker/login',CareTakerLoginView.as_view(),name="CareTaker Login"),
   # path('caretaker/register',CareTakeRegisterView.as_view(),name="CareTaker Registration"),

   # path('forgot-password/',LoginView.as_view(),name="Forgot Password"),
   # path('reset-password/',LoginView.as_view(),name="Password Reset"),

    #path('app/',),
   # path('caretaker/',include("caretaker.urls")),

]
