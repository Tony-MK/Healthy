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
	    extra_fields.setdefault('is_superuser', False)
	    return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
	    extra_fields.setdefault('is_superuser', True)
	    extra_fields.setdefault('is_staff', True);

	    if extra_fields.get('is_superuser') is not True:
	        raise ValueError('Superuser must have is_superuser=True.')

	    return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(blank=False,max_length=254,help_text="Email Address",editable=False,unique=True);
	id = models.UUIDField(default=uuid.uuid4,blank=False,primary_key=True,editable=False,unique=True);
	first_name = models.CharField(blank=False,max_length=128,help_text="First Name");
	last_name = models.CharField(blank=False,max_length=128,help_text="Surname");
	middle_name = models.CharField(blank=True,max_length=128,help_text="Middle Name");

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(help_text= 'active', default=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


	nationality = CountryField(blank=False,help_text="Country of Origin");
	primary_phone_number = PhoneField(blank=False,E164_only=False,help_text="Primary Phone Number");
	secondary_phone_number = PhoneField(blank=True,E164_only=False,help_text="Secondary Phone Number");

	date_of_birth = models.DateTimeField(blank=False,help_text="Date Of Birth");
	date_joined = models.DateTimeField(blank=False,help_text='Registration Date', auto_now_add=True)
	passport_number = models.CharField(blank=True,max_length=16,help_text="Passport Registration Number");

	GENDER_CHOICES = [("M","Male"),("F","Female")]
	gender = models.CharField(blank=False,max_length=2, choices=GENDER_CHOICES,help_text="User Sex");

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["primary_phone_number","first_name","last_name","date_of_birth","date_joined","gender"]

	objects = UserManager();

	def __str__(self):
		return "%s %s"%(self.first_name,self.last_name);

	pass



