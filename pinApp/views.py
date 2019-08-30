# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pinApp.forms import SimpleForm

def index(request):
	#return HttpResponse("Hello World!")
	myForm = SimpleForm()
	if request.POST.get('submit') == 'submit':
		
		print('Submit clicked')

	return render(request,"home.html",{'form':myForm})

# Create your views here.
