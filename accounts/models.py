from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
    #phone = models.CharField(max_length=70, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


 	# def __str__(self):
	# 	    return self.name


class Report(models.Model):
    STATUS =(
                ('Waiting','Waiting'),
                ('onTretamant', 'onTretamant'),
                ('Done','Done'),
            )
    CATEGORY = (
                     ('Animels','Animels'),
                     ('Safety Hazards','Safety Hazards'),
                     ('Car Accident','Car Accident'),
                     ('Signpost Damage','Signpost Damage'),
                     ('Weather Damage','Weather Damage'),
                     ('Other','Other'),
                )  
    URGENCY =   (    ('Immediate', 'Immediate'),
                     ('Medium','Medium'),
                     ('Not urgent','Not urgent'),
                )
#   user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, null=True)
    urgency = models.CharField(max_length=200,null=True, choices=URGENCY)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    location = models.CharField(max_length=200,null=True)
#   sub_topic = models.CharField(max_length=200,null=True, choices=SUB_TOPIC)
    details = models.TextField(max_length=200, null=True, blank=True)
#   complaint = models.ForeignKey(Complaint, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200,null=True, choices=STATUS)
    
    def __str__(self):
		    return self.name


# Create your models here.
