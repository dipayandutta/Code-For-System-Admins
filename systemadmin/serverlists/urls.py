from django.urls import path
from .views import (AddServers,CreateServerList,UpdateServerDetials,DeleteServerRecord)

urlpatterns = [
	path('addservers/',AddServers,name='addservers'),
	path('CreateServerList/',CreateServerList,name='createserver'),
	path('UpdateServerDetials/<int:SerialNumber>/',UpdateServerDetials,name='updateservers'),
	path('DeleteServerRecord/<int:SerialNumber>/',DeleteServerRecord,name='deleteserver'),
]