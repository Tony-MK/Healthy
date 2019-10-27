from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.template.loader import render_to_string
from django_countries.fields import CountryField
from django.utils.encoding import force_bytes
from .tokens import ActivationTokenGenerator
from django.core.mail import EmailMessage
from django.utils.timezone import now
from .user_manager import UserManager
from phone_field import PhoneField
from django.db import models
from decimal import Decimal
from uuid import uuid4


token_generator = ActivationTokenGenerator()

AVATAR_DIRECTORY = "static/avatars/"
MAX_NAME_LENGTH = 64
MAX_EMAIL_LENGTH = 128


class User(AbstractBaseUser,PermissionsMixin) :

	is_staff = models.BooleanField(
		blank=False,
		default=False,
	);

	is_superuser = models.BooleanField(
		blank=False,
		default=False,
	);

	is_active = models.BooleanField(
		blank=False,
		default=False
	);

	id = models.UUIDField(
		default=uuid4,
		unique=True,
		blank=False,
		null=False,
		primary_key=True,
		help_text="User Database Idenifition Number"
	)



	email = models.EmailField(
		blank=False,
		null=False,
		unique=True,
		max_length=MAX_NAME_LENGTH,
		help_text="Required. Email Address",
	);

	birth_date = models.DateField(
		null=True,
		blank=True,
		auto_now_add=False,
		help_text="Date Of Birth"
	);

	first_name = models.CharField(
		blank=False,
		null=False,
		max_length=MAX_NAME_LENGTH,
		help_text="Required. First Name"
	);

	last_name = models.CharField(
		null=True,
		blank=True,
		max_length=MAX_NAME_LENGTH,
		help_text="Optional. Family Name"
	);

	middle_name = models.CharField(
		null=True,
		blank=True,
		max_length=MAX_NAME_LENGTH,
		help_text="Optional. Middle Name"
	);

	phone_number = PhoneField(
		E164_only=True,
		null=True,
		blank=True,
		help_text="Primary Phone Number"
	);

	phone_number_confirmed = models.BooleanField(
		default=False,
		null=False,
		blank=False,
	)

	birth_certificate_number = models.CharField(
		null=True,
		blank=True,
		max_length=10,
		help_text="Birth Certificate Number"
	);

	nationality = CountryField(
		null=True,
		blank=True,
		help_text="Country of Origin"
	);

	national_id_number = models.CharField(
		null=True,
		blank=True,
		max_length=8,
		help_text="Kenyan Idenifition Number"

	);
	passport_number = models.CharField(
		null=True,
		blank=True,
		max_length=12,
		help_text="Passport Registration Number"
	);

	GENDER_CHOICES = [(0,"Not Specified"),(0,"Male"),(1,"Female")];

	gender = models.BinaryField(
		choices=GENDER_CHOICES,
		blank=True,
		null=True,
		max_length=1,
		default = None,
		help_text="User Sexual Orenitation"
	);

	avatar = models.ImageField(
		default= '/%s/default.jpg'%AVATAR_DIRECTORY,
		upload_to=AVATAR_DIRECTORY
	)
	

	USERNAME_FIELD = 'email';
	REQUIRED_FIELDS = ['first_name']

	objects = UserManager();

	def get_id_base64(self): 
		return urlsafe_base64_encode(force_bytes(self.id))

	def get_age(self): 
		return (self.date_of_birth - now).years

	def get_full_name(self):
		if self.last_name is None:
			return self.first_name

		mid_name = " "
		if self.middle_name is None:
			mid_name += self.middle_name

		return "%s%s %s"%(self.first_name,mid_name,self.last_name);

	def send_activation_email(self,):
		if (self.is_active):
			raise ValueError("User is Already Active")
		EmailMessage('Activation Token for %s\'s Account',
			render_to_string('auth/emails/activation.html',{
				'name':self.first_name,
				'b64id':self.get_id_base64(),
				'token':token_generator.make_token(self),
			}),to=[self.email]).send();

		pass;



	def __str__(self):
		return "%s (%s)"%(self.get_full_name(),self.email);
	pass





