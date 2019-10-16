from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
# Create your models here.
import uuid
from phone_field import PhoneField
from django_countries.fields import CountryField

class Patient(AbstractBaseUser):

    identifier = models.UUIDField(default=uuid.uuid4, editable=False);
    
    ID_FIELD = 'identifier'
    EMAIL_FIELD = models.EmailField(max_length=254);
    date_of_birth = models.DateTimeField();
    nationality = CountryField(blank=False)
    phone_number = PhoneField(blank=False,E164_only=False,help_text="Contact Phone Number");


    REQUIRED_FIELDS = ["date_of_birth","phone_number",""]
    


