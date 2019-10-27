# Create your views here.

from .models import Parent,CareTaker
from .forms import GigForm
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect,render
from django.views.generic import DetailView,FormView,TemplateView,View,ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class DashboardView(LoginRequiredMixin,TemplateView):
	template_name = "app/dashboard.html"

class ListView(ListView):
	template_name = "app/caretaker/list.html"
	context_object_name = 'users'
	model = CareTaker

	def get_queryset(self,):
		return CareTaker.objects.all();

class DetailView(DetailView):
	template_name = "app/caretaker/profile.html"
	model = CareTaker


