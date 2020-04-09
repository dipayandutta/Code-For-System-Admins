from django.db import models
from django.utils import timezone
# Create your models here.

class ServerDetails(models.Model):
	SerialNumber 	= models.AutoField(primary_key=True)
	CreatedAt		= models.DateField(default=timezone.now)
	ipaddress		= models.TextField(max_length=40)
	hdd				= models.TextField(max_length=30)
	ram				= models.TextField(max_length=30)
	core			= models.TextField(max_length=30)
	allocatedFor	= models.TextField(max_length=30)
	creationOrder	= models.TextField(max_length=30)
	os				= models.TextField(max_length=40)
	License			= models.TextField(max_length=60)
	createdBy		= models.TextField(max_length=100,default=None)