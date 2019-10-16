from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from .models import Child
from django.views.generic import TemplateView

class IndexView(TemplateView):
	"""docstring for IndexView"""
	template_name = 'app/index.html'


class AboutView(TemplateView):
	"""docstring for AboutView"""
	template_name = 'app/about.html'


class RegisterView(FormView):
	template_name = 'app/register.html'
	form_class = UserCreationForm();
	success_url  = '/register/sucess'
	def form_valid(self,form):
		form.save()
		email = form.cleaned_data.get('email');
		password = form.cleaned_data.get('password');
		if authenticate(username=username, password=raw_password) == None:
			return super().form_valid(form)
		

class LoginView(FormView):
	template_name = 'app/login.html'
	form_class = User.Form();

