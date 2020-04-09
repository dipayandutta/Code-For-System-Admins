from django.urls import path

from .views import (logpage,create)

urlpatterns = [
	path('addlog/',logpage,name='logpage'),
	path('create/',create,name='create'),
	
]