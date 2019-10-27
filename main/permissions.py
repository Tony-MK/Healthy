
#from django.contrib.auth.models import Permission,Group
#from .models import Appointment,CareTaker
# Parent Permission

"""
class CanBookAppointment(Permission):
	name = "Can Book Appointments"
	django_content_type  = "main_appointment"
	codename = "can_book_apppointment"

class CanViewAppointment(Permission):
	name = "Can Book Appointments"
	django_content_type  = "main_appointment"
	codename = "can_view_apppointment"

class CanSearchCareTaker(Permission):
	name = "Can Search CareTaker"
	django_content_type  = "main_careTaker"
	codename = "can_search_caretaker"

class CanViewCareTaker(Permission):
	name = "Can Search CareTaker"
	django_content_type  = "main_careTaker"
	codename = "can_view_caretaker"

DEAFULT_PARENT_PERMISSIONS = [
	CanViewAppointment,
	CanBookAppointment,
	CanViewCareTaker,
]

DEAFULT_CARETAKER_PERMISSIONS = [
	CanViewAppointment,
	CanSearchCareTaker,
]

class ParentGroup(object):
	docstring for ParentGroup'
	name =  "Parent Group"
	permissions = DEAFULT_PARENT_PERMISSIONS




class CaretakerGroup(object):
	docstring for CaretakerGroup'
	name =  "Caretaker Group"
	permissions = DEAFULT_CARETAKER_PERMISSIONS

"""