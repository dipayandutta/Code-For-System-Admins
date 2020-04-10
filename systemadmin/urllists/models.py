from django.db import models

# Create your models here.
class UrlLists(models.Model):
	SerialNumber 	= models.AutoField(primary_key=True)
	internalIP		= models.TextField(max_length=30)
	externalIP		= models.TextField(max_length=30)
	appName			= models.TextField(max_length=100)
	appURL			= models.TextField(max_length=200)
	Dept			= models.TextField(max_length=200) 