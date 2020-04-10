from django.urls import path
from .views import (home,signup,login,logout)

urlpatterns = [
	#path('',index,name="index"),
	path('home/',home,name="home"),
	path('signup/',signup,name="signup"),
	path('',login,name="login"),
	path('logout/',logout,name="logout")
]