from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import UrlLists
from django.core.paginator import Paginator
import urllib3
# Create your views here.

@login_required(login_url='/login/')
def urls(request):

	template = 'urllists.html'
	title    = 'urllists'

	applications 	= UrlLists.objects.all()
	paginator 		= Paginator(applications,5)
	page			= request.GET.get('page')
	applications 	= paginator.get_page('page')


	return render(request,template,{'title':title,'applications':applications})

@login_required(login_url='/login/')
def addApplications(request):
	deptartment 	= request.GET['dept']
	internalIP		= request.GET['internalIP']
	externalIP		= request.GET['externalIP']
	applicationName	= request.GET['applicationName']
	appURL			= request.GET['appURL']

	print(deptartment,internalIP,externalIP,applicationName,appURL)

	app_data = UrlLists(internalIP=internalIP,externalIP=externalIP,appName=applicationName,appURL=appURL,Dept=deptartment)
	app_data.save()

	return redirect('urls')

@login_required(login_url='/login/')
def urlstat(request):
	template 	= 'urlstat.html'
	title	 	= 'urlstat'

	result_status= []
	result_dict  = {}
	# store urls in the array fetech from the Database
	urls = UrlLists.objects.values_list('appURL',flat=True)
	http = urllib3.PoolManager()
	for url in urls:
		try:
			print(url)
			r = http.request('GET',url)
			result_status.append(r.status)
		except urllib3.exceptions.MaxRetryError as errRet:
			result_status.append("DOWN")

	result_dict = dict(zip(urls,result_status))

	print(result_dict)
	return render(request,template,{'title':title,'result_dict':result_dict})