from django import forms 

class Select(forms.Select):
	template_name = "django/forms/widgets/healthy_select.html"

class EmailInput(forms.EmailInput):
	template_name = "django/forms/widgets/healthy_email.html"

class PasswordInput(forms.PasswordInput):
	template_name = "django/forms/widgets/healthy_password.html"

class TextInput(forms.TextInput):
	template_name = "django/forms/widgets/healthy_text.html"

class DateInput(forms.DateInput):
	template_name = "django/forms/widgets/healthy_date.html"

class TimeInput(forms.TimeInput):
	template_name = "django/forms/widgets/healthy_time.html"
