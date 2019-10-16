# Create your views here.
from .models import Child,CareTaker
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import DetailView,FormView,TemplateView
from .forms import SignUpForm,LoginUpForm


class IndexView(TemplateView):
	"""docstring for IndexView"""
	template_name = 'main/index.html'


class AboutView(TemplateView):
	"""docstring for AboutView"""
	template_name = 'main/about.html'



class ChildRegisterView(FormView):
	template_name = 'auth/register.html'
	form_class = SignUpForm;
	success_url  = '/register/sucess'
	def form_valid(self,form):
		form.save()

		email = form.cleaned_data.get('email');
		password = form.cleaned_data.get('password1');
		try:
			child = Child(username=username,password=password,first_name=form.cleaned_data.get('first_name'))
			child.Create_user();
			return super().form_valid(form)
		except Exception as e:
			print(e)
			return super().form_invalid(form)
		
		


class LoginView(FormView):
	template_name = 'auth/login.html';
	form_class = LoginUpForm;
	success_url  = '/cholde'
	def form_valid(self,form):
		email = form.cleaned_data.get('email');
		password = form.cleaned_data.get('password');
		user = authenticate(email=email, password=password)
		if user == none:
			return super().form_invalid(form);
		return super().form_invalid(form);

