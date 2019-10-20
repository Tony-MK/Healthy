# Create your views here.


from .models import Child,CareTaker
from .forms import ChildRegisterForm,CareTakerRegisterForm,LogInForm

from django.contrib.auth import authenticate


from django.shortcuts import redirect

from django.views.generic import DetailView,FormView,TemplateView
from datetime import timedelta


CHILD_AGE_MAX_LIMIT = 17
CHILD_AGE_MIN_LIMIT = 6


class IndexView(TemplateView):
	"""docstring for IndexView"""
	template_name = 'main/index.html'


class AboutView(TemplateView):
	"""docstring for AboutView"""
	template_name = 'main/about.html'




###		 AUTH 		###

def activate(req, b64id, token):
	try:
		user = User.objects.get(pk=force_text(urlsafe_base64_decode(b64id)));
		if token_generator.check_token(user, token):
			user.is_active = True;
			user.save();
			return HttpResponse("Successfully activacted Account");
		return HttpResponse("Wrong or Expired Token");

	except(User.DoesNotExist):
		return HttpResponse("User does not exist");

	except(TypeError, ValueError, OverflowError):
		return HttpResponse("Invalid Token");

	except Exception as e:
		raise e;




class ChildRegisterView(FormView):
	template_name = 'auth/register.html'
	form_class = ChildRegisterForm;
	success_url  = '/email_comfiration'
	def form_valid(self,form):
		child = form.save(commit=False);
		child.is_child = True;
		child.is_active = False;
		child.send_activation_email();
		child.save()
		return super().form_valid(form);

"""
class CareTakerRegisterView(FormView):
	template_name = 'auth/register_caretaker.html'
	form_class = CareTakerRegisterForm;
	success_url  = '/register/sucess'
	def form_valid(self,form):
		form.save();
		email = form.cleaned_data.get('email');
		try:
			caretaker = CareTaker.objects.get(email=email);
			redirect('/caretaker/login');

		except DoesNotExist:

			CareTaker.create_user(email=email,
				password=form.cleaned_data.get('password1'),
				first_name=form.cleaned_data.get('first_name'),
				family_name=form.cleaned_data.get('family_name'),
				idenfition_number=form.cleaned_data.get('idenfition_number'),
				gender=form.cleaned_data.get('gender'),
				phone_numeber=form.cleaned_data.get('gender'),
				date_of_birth=form.cleaned_data.get('date_of_birth'),
			)

			return super().form_valid(form)

		except Exception as e:
			print(e)
"""


def getFullUser(email):
	try:
		return Child.objects.get(email=email)
	except Exception as e:
		try:
			return CareTaker.objects.get(email=email)
		except Exception as e:
			return None;


class ChildLoginView(FormView):
	template_name = 'auth/login.html';
	form_class = LogInForm;
	success_url = "child"
	def form_valid(self,form):
		try:
			Child.objects.get(email=email);
			if authenticate(email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password')):
				login(request,user);
				return super().form_valid(form);
		except Exception as e:
			raise e
		return super().form_invalid(form);

class CareTakerLoginView(FormView):
	template_name = 'auth/login.html';
	form_class = LogInForm;
	success_url = "caretaker"
	def form_valid(self,form):
		try:
			ChilCareTaker.objects.get(email=email);
			if authenticate(self.request,email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password')):
				login(request,user);
				return super().form_valid(form);
			return super().form_invalid(form);
		except Exception as e:
			raise e
		return super().form_invalid(form);



