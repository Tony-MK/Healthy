from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import Child,CareTaker,User


DATE_FORMATS = ['%d/%m/%y','%d/%m/%Y','%m/%d/%y','%m/%d/%Y','%m-%d-%Y','%m-%d-%y','%Y-%m-%d']

class CareTakerRegisterForm(UserCreationForm):
	date_of_birth = forms.DateField(input_formats=DATE_FORMATS)

	class Meta:
		model = CareTaker
		fields = ('first_name','gender','date_of_birth','phone_number','email')
		pass;


class ChildRegisterForm(UserCreationForm):
	date_of_birth = forms.DateField(input_formats=DATE_FORMATS)
	class Meta:
		model = Child
		fields = ('first_name','gender','date_of_birth','email')
		pass;



class LogInForm(AuthenticationForm):

	class Meta:
		model = User
		fields = ('email','password');


class PasswordResetForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('password');





