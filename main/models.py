from django.db import models
from .user import User
class Child(User):
	pass;

class CareTaker(User):
	idenfition_number = models.CharField(blank=False,max_length=16,unique=True,editable=False);
