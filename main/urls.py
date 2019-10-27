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
from django.contrib.auth.decorators import login_required


from .views import *
from .views_app import *
from .views_caretaker import *
from . import views_parent as parent
from . import views_gig as gig


urlpatterns = [
    
    url(r'^Help/$',
        LogOutView.as_view(),
        name="Help",
    ),



    url(r'^login/$',
        LoginView.as_view(template_name = 'auth/parent_login.html'),
        name="Login",

    ),

    url(r'^caretaker/login/$',
        LoginView.as_view(template_name = 'auth/caretaker_login.html'),
        name="Caretaker Login"
     ),

    url(r'^register/$',ParentRegisterView.as_view(),name="Register"),

    url(r'^caretaker/register/$',CaretakerRegisterView.as_view(),name="Caretaker Register"),

    url(r'^logout/$',LogOutView.as_view(),name="Logout"),
    url(r'^email_confirmation/$',EmailConfirmationView.as_view(),name="Email Confirmation"),
    url(r'^activate/(?P<b64id>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate,name="Activate"),
    path('forgot-password/',LogOutView.as_view(),name="Forgot Password"),


    # --- All --- #

    path('app/',DashboardView.as_view(),name="Dashboard"),
    path('app/hire/<slug:pk>',HireView.as_view(),name="Hire"),

   # path('app/hire/request/<slug:pk>',HireRequestView.as_view(),name="Hire Request"),
    path('app/hire/success/<slug:pk>',HireSuccessView.as_view(),name="Hire Success"),
   # path('app/view/<slug:pk>',GigView.as_view(),name="Gig View"),

   # path('app/profile/edit',ProfileEditView.as_view(),name="Profile Edit"),

    # --- Parent --- #
    path('app/parent/dashboard/',parent.DashboardView.as_view(),name="Parent Dashboard"),
    path('app/parent/profile/',parent.ProfileView.as_view(),name="Parent Profile"),
    path('app/parent/profile/',parent.ProfileView.as_view(),name="Profile Edit"),
    path('app/parent/profile/',parent.ProfileView.as_view(),name="Calendar"),


    # --- Parent Gigs --- 
    path('app/gig/list',gig.ListView.as_view(),name="List Gig"),
    path('app/gig/create/',gig.CreateView.as_view(),name="Create Gig"),
    path('app/gig/detail/<slug:pk>',gig.DetailView.as_view(),name="Detail Gig"),
    path('app/gig/change/<slug:pk>',gig.ChangeView.as_view(),name="Edit Gig"),
    path('app/gig/cancel/<slug:pk>',HireView.as_view(),name="Cancel Gig"),


    path('account/profile/',parent.ProfileView.as_view(),name="Profile"),



    # --- Caretaker --- #

    path('app/caretaker/list',ListView.as_view(),name="Caretaker list"),
    path('app/caretaker/profile/<slug:pk>',DetailView.as_view(),name="Caretaker Profile"),



]
