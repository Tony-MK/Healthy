from django.contrib.auth.forms import UserCreationForm
from django import forms
from .user import User

class  SignUpForm(UserCreationForm):
	"""docstring for  SignUpForm"""

	first_name = forms.CharField(max_length=30,required=False,help_text="Required. Your First Name");
	last_name = forms.CharField(max_length=30,required=False,help_text="Required. Your First Name");

	email = forms.EmailField(max_length=30,required=False,help_text="Required. Your First Name");

	def __init__(self, arg):
		super( SignUpForm, self).__init__()
		self.arg = arg
