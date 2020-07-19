import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from  .models import Report
from django.contrib.auth.models import User
from  .models import Customer
#from  .models import Complaint


class reportFilter(django_filters.FilterSet):

	class Meta:
		model = Report
		fields = ['urgency','category','status']
		#exclude = ['customer', 'date_created','Complaint','Deatils']

class userFilter(django_filters.FilterSet):

	class Meta:
		model = Customer
		fields = ['email']
		