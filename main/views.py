from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from .models import Patient

class IndexView(DetailView):
	"""docstring for IndexView"""
	template_name = 'app/index.html'


class LoginView(DetailView):
	template_name = 'app/login.html'
	context  = Patient();


class RegisterView(DetailView):
	template_name = 'app/register.html'
