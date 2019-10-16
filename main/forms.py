from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .user import User
from phone_field import PhoneField
from  django_countries.fields import CountryField

DATE_FORMATS = ['%m/%d/%Y','%m/%d/%y','%m-%d-%Y','%m-%d-%y','%Y-%m-%d']

class  SignUpForm(UserCreationForm):
	gender = forms.ChoiceField(required=True,choices=User.GENDER_CHOICES,help_text="User Sex");
	date_of_birth = forms.DateField(input_formats=DATE_FORMATS , )
	email = forms.EmailField(max_length=30,required=True,help_text="Required. An Email Address eg.. Gmail, YahooMail ");

	class Meta:
		model = User
		fields = ('first_name','gender','date_of_birth','email')
	


class  LoginUpForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('email','password');

