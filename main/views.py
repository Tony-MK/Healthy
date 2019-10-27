# Create your views here.

from .user import User,token_generator
from .models import Parent,CareTaker
from .forms import CaretakerRegisterForm,ParentRegisterForm,LogInForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import views


from django.shortcuts import redirect,render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView,TemplateView
from datetime import timedelta



decodeBase64Data = lambda data: force_text(urlsafe_base64_decode(data))


###		 AUTH 		###

class LoginView(FormView):
	form_class = LogInForm;
	success_url = "/app/";

	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect(request,self.success_url);
		return super().get(self,request,*args,**kwargs) 

	def post(self,request,*args,**kwargs):

		if request.user.is_authenticated:
			return redirect(request,self.success_url);

		form = self.get_form();
		if not form.is_valid():
			return super().form_invalid([form,ValueError("Invalid Form")]);

		form.clean()
		user = authenticate(email=form.cleaned_data.get("email"),password=form.cleaned_data.get("password"));
		print(" Email: {} Password: {}".format(form.cleaned_data.get("email"),form.cleaned_data.get("password")))

		if user is None:
			return super().form_invalid([form,ValueError("Incorrect Email or Password")]);

		login(request,user)
		return super().form_valid(form);


class LogOutView(views.LogoutView):
	next_page = "/login"


class ParentRegisterView(FormView):
	success_url  = '/email_confirmation/'
	form_class = ParentRegisterForm;
	template_name = 'auth/parent_register.html'
	def form_valid(self,form):
		parent = form.save(commit=False);
		parent.save();
		parent.send_activation_email();
		return super().form_valid(form);

class CaretakerRegisterView(FormView):
	success_url  = '/email_confirmation/'
	form_class = CaretakerRegisterForm;
	template_name = 'auth/caretaker_register.html'
	def form_valid(self,form):
		caretaker = form.save(commit=False);
		caretaker.save();
		caretaker.send_activation_email();
		return super().form_valid(form);

class EmailConfirmationView(TemplateView):
	"""docstring for EmailConfirmationView"""
	template_name = "auth/activation_prompt.html"


def activate(request, b64id, token):
	ctx = {"token":token}
	pk = decodeBase64Data(b64id);
	try:
		user = User.objects.get(pk=pk);
		if user is None:
			ctx["title"] = "No User Found";
			ctx["msg"] =  "No User was Found with ia primary key of "+user.pk;
		elif token_generator.check_token(user, token):
			user.is_active = True;

			user.save();
			ctx["name"] = user.first_name
			return render(request,"auth/activation_success.html",ctx);
		else:
			ctx["title"] = "Token Authorization Failed";
			ctx["msg"] = "Token is used or Expired";

	except(User.DoesNotExist):
		ctx["title"] = "User Error";
		ctx["msg"] = "No User was Found with a primary key of "+pk;


	except(TypeError, ValueError, OverflowError):
		ctx["title"] = "Invalid Token";
		ctx["msg"] = "Token has many an issue";

	except Exception as e:
		ctx["title"] = "Unknown Error";
		ctx["msg"] = e;

	return render(request,"auth/activation_failure.html",ctx)



