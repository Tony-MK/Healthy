# Create your views here.

from .models import Parent,CareTaker,Gig
from .forms import GigForm
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect,render
from django.views.generic import DetailView,TemplateView,View,ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.utils.timezone import now 
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from datetime import datetime
import pytz


DATE_FORMAT,TIME_FORMAT = "%Y-%m-%d","%H:%M";
DATETIME_FORMAT = DATE_FORMAT +" "+ TIME_FORMAT
def parse_datetime(date,time):
	return 

def format_datetime(date,time):
	return datetime.strptime('%s %s'%(date.strftime(DATE_FORMAT),time),DATETIME_FORMAT).replace(tzinfo=pytz.UTC)

class CreateView(FormView,PermissionRequiredMixin):
	template_name = "app/gig/create.html"
	form_class = GigForm


	def post(self,req,*args, **kwargs):
		form = self.get_form();
		if form.is_valid():
			try:
				err = self.create_gig(form,by=Parent.objects.get(pk=req.user.pk));
				if err is None:
					return err
				self.success_url = "/app/gig/detail/"+req.user.pk.__str__()
				return super().form_valid(form)
			except Parent.DoesNotExist:
				return redirect(req,"/app/")
		return super().form_invalid(form);

	def create_gig(self,form,by):
		data = form.clean();
		gig = Gig(by=by,start=format_datetime(data["start_date"],data["start_time"]))
		try:
			gig.validate_start();
		except ValueError as e:
			return super().form_invalid([form,{"start_date":e}]);

		try:
			gig.end = format_datetime(data["end_date"],data["end_time"]);
			gig.validate_duration();
		except ValueError as e:
			return super().form_invalid([form,{"end_date":e}])

		gig.notes = data["notes"]
		gig.save();
		pass

		
		

class DetailView(DetailView,PermissionRequiredMixin):
	template_name = "app/gig/detail.html"
	model = Gig;

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class ListView(ListView,PermissionRequiredMixin):
	template_name = "app/gig/list.html"
	context_object_name = 'gigs'
	model = Gig;

	def get_queryset(self,):
		return Gig.objects.all();



class ChangeView(FormView):
	template_name = "app/change.html"
	form_class = GigForm;
	permission_required = "main.can_book_Gig"

	def vaild_form(self,form):
		return super().vaild_form(form)

class CancelGigView(View):
	template_name = "app/cancel.html"
	form_class = GigForm
	permission_required = "main.can_book_Gig"


	@method_decorator(login_required)
	def render_to_response(self,cxt, **kwargs):
		super().render_to_response(cxt, **kwargs)

	@method_decorator(login_required)
	def vaild_form(self,form):
		return super().vaild_form(form)

