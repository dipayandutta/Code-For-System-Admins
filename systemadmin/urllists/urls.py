from django.urls import path
from .views import urls,addApplications,urlstat

urlpatterns = [
	path('lists/',urls,name='urls'),
	path('addApps/',addApplications,name='addApps'),
	path('stat/',urlstat,name='stat'),
]