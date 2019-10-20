

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django_countries.fields import CountryField
from .user_manager import UserManager
from phone_field import PhoneField
from django.utils.timezone import now
from django.db import models
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.mail import EmailMessage
from uuid import uuid4
from decimal import Decimal
from .tokens import TokenGenerator;

token_generator = TokenGenerator()



# Create your models here.

MIN_HEIGHT = '0.50000';
MAX_HEIGHT = '3.00000';
heightValidator = [MinValueValidator(Decimal(MIN_HEIGHT)),MaxValueValidator(Decimal(MAX_HEIGHT))]

MIN_WEIGHT = '10.00';
MAX_WEIGHT = '158.00';
weightValidator = [MinValueValidator(Decimal(MIN_WEIGHT)),MaxValueValidator(Decimal(MAX_WEIGHT))]

class User(AbstractBaseUser,PermissionsMixin) :

	
	id = models.UUIDField(blank=False,default=uuid4,primary_key=True,unique=True);
	email = models.EmailField(blank=False,max_length=254,help_text="Email Address",unique=True);

	date_joined = models.DateTimeField(default=now,blank=False,help_text='Registration Date',)
	date_of_birth = models.DateField(blank=False,auto_now_add=False,help_text="Required. The Day you were Born.Address same as on your Birth Certificate");

	first_name = models.CharField(blank=False,max_length=128,help_text="Required. Your First Name, same as on your Birth Certificate");
	family_name = models.CharField(max_length=128,help_text="Family Name");
	middle_name = models.CharField(max_length=128,help_text="Middle Name");

	birth_certificate_number = models.CharField(max_length=16,help_text="Birth Certificate Number");
	passport_number = models.CharField(max_length=16,help_text="Passport Registration Number");

	nationality = CountryField(help_text="Country of Origin");
	phone_number = PhoneField(E164_only=False,help_text="Primary Phone Number");

	#height = models.DecimalField(help_text='Height (cm)', decimal_places=5, max_digits=6, validators=heightValidator);
	#weight = models.DecimalField(help_text='Weight (cm)', decimal_places=2, max_digits=5, validators=weightValidator);
	
	GENDER_CHOICES = [("M","Male"),("F","Female")]
	gender = models.CharField(blank=False,max_length=2, choices=GENDER_CHOICES,help_text="User Sex");

	#avatar = models.ImageField(default='avatars/default.png',editable=True,upload_to='avatars/')

	is_staff = models.BooleanField(blank=False,default=False);
	is_superuser = models.BooleanField(blank=False,default=False);
	is_active = models.BooleanField(blank=False,default=False);
	is_child = models.BooleanField(blank=False,default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name","gender",]

	objects = UserManager();

	def __str__(self):
		return "%s %s"%(self.first_name,self.family_name);
		pass
	pass



class Child(User):
	

	def getAge(self):
		return self.date_of_birth - now

	def send_activation_email(self,):
		EmailMessage(
				"Healthy Child Account Activation",
				render_to_string('auth/emails/activation.html',{
					'name':self.first_name,
					'b64id':urlsafe_base64_encode(force_bytes(self.id)),
					'token':token_generator.make_token(self),
				}),
				to=[self.email]
			).send();
		pass;
	pass;


class CareTaker(User):
	idenfition_number = models.CharField(blank=False,max_length=8,unique=True);

	




