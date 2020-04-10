from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from serverlists.models import ServerDetails
# Create your views here.
'''
def index(request):
	template = 'home.html'
	title = 'index'
	return render(request,template,{'title':title})
'''
@login_required(login_url='/login/')
def home(request):

	total_blade_storage = 10,240
	title = 'Dashboard'
	#Calculation for Total Number of servers
	ipaddress_total = ServerDetails.objects.values_list('ipaddress',flat=True)
	ipaddress_total_count = len(ipaddress_total)

	# Calculation for server OS Clustering
	os_total 		= ServerDetails.objects.values_list('License',flat=True)
	linux_os 		= 0
	microsoft_os  	= 0
	
	for os_license in os_total:
		if os_license == 'opensource':
			linux_os+=1
		else:
			microsoft_os+=1
	
	# Calculation for Total used Storage
	total_used_storage = ServerDetails.objects.values_list('hdd',flat=True)

	storage = 0
	for strg in total_used_storage:
		storage += int(strg)
		print(storage)


	# Calculation for Total Cores Used
	total_core_used   = ServerDetails.objects.values_list('core',flat=True)

	cores = 0
	for core in total_core_used:
		cores += int(core)
		print (cores)

	#Calucation for Total RAM Used
	total_ram_used    = ServerDetails.objects.values_list('ram',flat=True)

	rams = 0
	for ram in total_ram_used:
		rams += int(ram)
		print(rams)

	return render(request,'home.html',{'title':title,'total_servers':ipaddress_total_count,'linux_servers':linux_os,'microsoft_servers':microsoft_os,'used_storeged':storage,'total_blade_storage':total_blade_storage,'cores':cores,'rams':rams})


def signup(request):
	template = 'signup.html'
	title    = 'signup'

	if request.method == 'POST':
		username 		= request.POST['username']
		passwordFirst	= request.POST['password1']
		passwordSecond	= request.POST['password2']
		email			= request.POST['emailid']

		if passwordFirst == passwordSecond:
			try:
				user = User.objects.get(username=username)
				return render(request,template,{'error':'username already exists!'})
			except User.DoesNotExist:
				user = User.objects.create_user(username,password=passwordFirst,email=email)
				return render(request,template,{'message':'User Created Successfully!'})
	return render(request,template,{'title':title})

def login(request):
	template = 'login.html'
	title 	 = 'login'

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,template,{'error':'username or password mismatch'})
	return render(request,template,{'title':title})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')