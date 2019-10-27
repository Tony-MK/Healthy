from django.core.validators import MinValueValidator,MaxValueValidator
from django.template.loader import render_to_string
from django.utils.timezone import now 
from decimal import Decimal
from .user import User
from django.db.models import *
from uuid import uuid4
from datetime import timedelta



#from .permissions import *

MAX_TEXT_LENGTH = 512;
MIN_RATING, MAX_RATING = '0.00','7.00';
MIN_GIG_HOURS = 1
MIN_GIG_DELTA = timedelta(hours=MIN_GIG_HOURS)

rating_validator = [MinValueValidator(Decimal(MIN_RATING)),MaxValueValidator(Decimal(MAX_RATING))]

MIN_HEIGHT = '0.50000';
MAX_HEIGHT = '3.00000';
heightValidator = [MinValueValidator(Decimal(MIN_HEIGHT)),MaxValueValidator(Decimal(MAX_HEIGHT))]

MIN_WEIGHT = '10.00';
MAX_WEIGHT = '158.00';
weightValidator = [MinValueValidator(Decimal(MIN_WEIGHT)),MaxValueValidator(Decimal(MAX_WEIGHT))]



# Create your models here.

class Location(Model):
	unit = CharField(blank=True,null=True,max_length=8);
	complex_name = CharField(blank=True,null=True,max_length=64);
	street = CharField(blank=False,max_length=64);
	area = CharField(blank=False,max_length=64);
	nearby_landmark = CharField(blank=True,null=True,max_length=64);


class CareTaker(User):
	overall_rating = DecimalField(default=Decimal(MIN_RATING),help_text='Overall Rating', decimal_places=2, max_digits=3, validators=rating_validator);
	
	def parse_card(self):
		return render_to_string('app/caretaker/card.html',{'user':self})

	def parse_checkbox(self):
		return render_to_string('/app/caretaker/input.html',{'user':self})


	class Meta:
		"""docstring for Meta"""
		#proxy = True;
		#permissions = [('can_cancel_apppointment','can_view_apppointment','can_list_apppointment','can_view_apppointment','can_search_caretaker','can_view_caretaker',)]
	pass;


class Parent(User):
	residence = ForeignKey(Location,null=True,blank=True,on_delete=DO_NOTHING)
	favorite_caretakers = ForeignKey(CareTaker,blank=True,null=True,on_delete=DO_NOTHING)
	class Meta:
		"""docstring for Meta"""
		#proxy = True;
		permissions = [('can_book_apppointment',"Can Book Gig")]
	pass;
	

"""
class Child(User):
	height = DecimalField(null=True,blank=True,help_text='Height (cm)', decimal_places=5, max_digits=6, validators=heightValidator);
	weight = DecimalField(null=True,blank=True,help_text='Weight (cm)', decimal_places=2, max_digits=5, validators=weightValidator);
	

	class Meta:
		docstring for Meta
		proxy = True;
		permissions = [('can_view_apppointment','can_search_caretaker','can_view_caretaker',)]
	pass;
"""
class Submisssion(Model):
	STATUS_CHOICES = [(None,"Pending Approval"),(1,"Rejected"),(2,"Approved")];
	REQUIRED_FIELDS = ["by","status"]

	by = ForeignKey(CareTaker,blank=True,null=False,on_delete=DO_NOTHING,);
	notes = CharField(blank=False,null=True,max_length=MAX_TEXT_LENGTH);

	status = BinaryField(blank=False,null=True,choices=STATUS_CHOICES,default=None)



class Gig(Model):
	"""docstring for Gig"""

	id = UUIDField(default=uuid4,primary_key=True,unique=True,editable=False,)
	created = DateTimeField(blank=False,null=False,auto_now_add=False,default=now);

	by = ForeignKey(Parent,on_delete=DO_NOTHING);
	start  = DateTimeField(blank=False,null=False,auto_now_add=False);
	end = DateTimeField(blank=False,null=False,auto_now_add=False);
	notes = CharField(blank=False,null=True,max_length=MAX_TEXT_LENGTH);

	submissions = ManyToManyField(Submisssion);

	REQUIRED_FIELDS = ['creator','start_date','end_date']

	def __str__(self):
		return "{} {}".format(self.by.first_name,self.start)
		
	def validate_duration(self):
		print("Duration")
		if self.start+MIN_GIG_DELTA < self.end:
			raise(ValueError("Gig duration Can Not Be less than %d hours."%MIN_GIG_HOURS))

	def validate_start(self):
		print("Start",now(),self.start)
		if self.start < now():
			raise(ValueError("Can not setted start time which has already passed"));





	



		
			





