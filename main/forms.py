from django.contrib.auth.forms import UserCreationForm
from django.forms import Form,CharField,DateField,DateTimeField,EmailField,ChoiceField
from .form_inputs import *
from .models import Parent,CareTaker,User,Gig,Location



class CaretakerRegisterForm(UserCreationForm):
	"""docstring for CaretakerRegisterForm"""

	first_name = CharField(widget= TextInput(attrs={"label":"First Name","icon":"single-02"}),required=True,)
	email = EmailField(widget=EmailInput(attrs={"label":"Email Address"}),required=True)
	password1 = CharField(widget=PasswordInput(attrs={"label":"Sercet Password"}),required=True)
	password2 = CharField(widget=PasswordInput(attrs={"label":"Confirm your Sercet Password "}),required=True)

	class Meta:
		model = CareTaker
		fields = ('first_name','email','password1','password2')
		pass;


class ParentRegisterForm(UserCreationForm):
	"""docstring for ParentRegisterForm"""

	first_name = CharField(widget= TextInput(attrs={"label":"First Name","icon":"single-02"}),required=True,)
	email = EmailField(widget=EmailInput(attrs={"label":"Email Address"}),required=True)
	password1 = CharField(widget=PasswordInput(attrs={"label":"Sercet Password"}),required=True)
	password2 = CharField(widget=PasswordInput(attrs={"label":"Confirm your Sercet Password "}),required=True)

	class Meta:
		model = Parent
		fields = ('first_name','email','password1','password2')
		pass;


		
class LogInForm(Form):
	email = EmailField(widget=EmailInput(attrs={"label":"Email"}),required=True)
	password = CharField(widget=PasswordInput(attrs={"label":"Password"}),required=True)
	class Meta:
		model = User
		fields = ('email','password')
		pass




class GigForm(Form):
	start_date = DateField(
		widget= DateInput(attrs={"label":"Begining Time"}),
		required=True,
	)

	start_time = CharField(
		widget= TimeInput(attrs={"label":"Begining Time"}),
		required=True,
	)

	end_date = DateField(
		widget= DateInput(attrs={"label":"Finish Date"}),
		required=True,
	)

	end_time = CharField(
		widget= TimeInput(attrs={"label":"Finish Time"}),
		required=True,
	)

	notes  = CharField(
		widget= TextInput(attrs={"label":"Anything you would like share","icon":"key-50"}),required=True,
	);


	class Meta:
		model = Gig
		fields = ('start_date','end_date','location','caretaker','notes')
		pass;


