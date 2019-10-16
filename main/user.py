from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django_countries.fields import CountryField
from django.utils import timezone
from phone_field import PhoneField
import uuid
# Create your models here.


class UserManager(BaseUserManager):
	"""docstring for  UserManager"""
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
	    """
	    Creates and saves a User with the given email and password.
	    """
	    if not email:
	        raise ValueError('The given email must be set')
	    email = self.normalize_email(email)
	    user = self.model(email=email, **extra_fields)
	    user.set_password(password)
	    user.save(using=self._db)
	    return user

	def create_user(self, email, password=None, **extra_fields):
	    extra_fields.setdefault('is_superuser', False);
	    extra_fields.setdefault('is_staff',False);
	    extra_fields.setdefault('is_active',False);
	    return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_staff', True);
		return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):

	
	id = models.UUIDField(blank=False,default=uuid.uuid4,primary_key=True,unique=True);
	email = models.EmailField(blank=False,max_length=254,help_text="Email Address",unique=True);

	date_joined = models.DateTimeField(blank=False,help_text='Registration Date', auto_now_add=True)
	date_of_birth = models.DateField(blank=False,help_text="Required. The Day you were Born.Address same as on your Birth Certificate");

	first_name = models.CharField(blank=False,max_length=128,help_text="Required. Your First Name, same as on your Birth Certificate");
	family_name = models.CharField(max_length=128,help_text="Family Name");
	middle_name = models.CharField(max_length=128,help_text="Middle Name");

	birth_certificate_number = models.CharField(max_length=16,help_text="Birth Certificate Number");
	passport_number = models.CharField(max_length=16,help_text="Passport Registration Number");

	nationality = CountryField(help_text="Country of Origin");
	phone_number = PhoneField(E164_only=False,help_text="Primary Phone Number");
	
	GENDER_CHOICES = [("M","Male"),("F","Female")]
	gender = models.CharField(blank=False,max_length=2, choices=GENDER_CHOICES,help_text="User Sex");

	#avatar = models.ImageField(default='avatars/default.png',editable=True,upload_to='avatars/')

	is_staff = models.BooleanField(blank=False,default=False,)
	is_superuser = models.BooleanField(blank=False,default=False,);
	is_active = models.BooleanField(blank=False,default=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name","date_joined","gender"]

	objects = UserManager();

	def __str__(self):
		return "%s %s"%(self.first_name,self.last_name);

	pass



