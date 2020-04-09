from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import LogBookEntry
# Create your views here.

@login_required(login_url='/login/')
def logpage(request):
	template = 'serverlogs.html'
	title    = 'serverlogs'
	logs 	 = LogBookEntry.objects.all()
	
	return render(request,template,{'title':title,'logs':logs})

@login_required(login_url='/login/')
def create(request):

	author 		= request.GET['author']
	designation	= request.GET['designation']
	subject		= request.GET['subject']
	reportedto	= request.GET['reportedto']
	instructedby= request.GET['instructedby']

	print(author)
	print(designation)
	print(subject)
	print(reportedto)
	print(instructedby)

	log_to_store = LogBookEntry(Author=author,Designation=designation,Subject=subject,ReportedTo=reportedto,InstructedBy=instructedby)
	log_to_store.save()

	return redirect('logpage')

