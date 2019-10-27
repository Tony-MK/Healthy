# Create your views here.

from .models import Parent,CareTaker,Gig
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


class HireView(DetailView,FormView,PermissionRequiredMixin):
	template_name = 'app/hire.html'
	
	model = CareTaker

	def get_context_data(self,**kwargs):
		ctx =  super().get_context_data(**kwargs);
		ctx["form"] = GigForm
		return ctx

	def post(self, req,*args, **kwargs):
		self.object = self.get_object();
		return super().post(req,*args, **kwargs);

	def get_success_url(self):
		return reverse('Hire Success', kwargs={'pk': self.object.pk})

	def form_valid(self,form):
		gig = form.clean();

		print(form);
		return super().form_valid();


class HireSuccessView(DetailView,PermissionRequiredMixin):
	template_name = "app/hire_success.html"

class HireFailure(DetailView,PermissionRequiredMixin):
	template_name = "app/hire_fail.html"
