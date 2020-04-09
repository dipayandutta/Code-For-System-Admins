from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import ServerDetails
# Create your views here.

@login_required(login_url='/login/')
def AddServers(request):
	title 		= 'Add Servers'
	template	= 'addservers.html'
	servers     = ServerDetails.objects.all()
	paginator 	= Paginator(servers,5)
	page 		= request.GET.get('page')
	servers 	= paginator.get_page(page)

	# get total number of servers using IPAddress
	ipaddress_total = ServerDetails.objects.values_list('ipaddress',flat=True)
	ipaddress_total_count = len(ipaddress_total)
	return render(request,template,{'title':title,'servers':servers,'total_servers':ipaddress_total_count})


@login_required(login_url='/login/')
def CreateServerList(request):

	ipaddress 		= request.GET['ipaddress']
	hdd		  		= request.GET['hdd']
	ram		  		= request.GET['ram']
	core	  		= request.GET['core']
	allocatedFor	= request.GET['allocatedFor']
	creationOrder	= request.GET['creationOrder']
	os				= request.GET['os']
	License			= request.GET['license']
	createdBy		= request.GET['createdBy']

	print(ipaddress,hdd,ram,core,allocatedFor,creationOrder,os,License,createdBy)

	store_servers = ServerDetails(ipaddress=ipaddress,hdd=hdd,ram=ram,core=core,allocatedFor=allocatedFor,creationOrder=creationOrder,os=os,License=License,createdBy=createdBy)
	store_servers.save()
	return redirect('addservers')

@login_required(login_url='/login/')
def UpdateServerDetials(request,SerialNumber):

	server 				= ServerDetails.objects.get(pk=SerialNumber)

	server.ipaddress	= request.GET['ipaddress']
	server.hdd			= request.GET['hdd']
	server.ram			= request.GET['ram']
	server.core 		= request.GET['core']
	server.allocatedFor = request.GET['allocatedFor']
	server.creationOrder= request.GET['creationOrder']
	server.os 			= request.GET['os']
	server.License 		= request.GET['license']
	server.createdBy	= request.GET['createdBy']

	print(server.ipaddress,server.hdd,server.ram,server.core,server.allocatedFor,server.creationOrder,server.os,server.License,server.createdBy)
	server.save()

	return redirect('addservers')

@login_required(login_url='/login/')
def DeleteServerRecord(request,SerialNumber):
	server 				= ServerDetails.objects.get(pk=SerialNumber)
	server.delete()

	return redirect('addservers')