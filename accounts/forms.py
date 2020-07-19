from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Report
#from .models import Complaint


class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ['name','category','location','urgency','details']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']