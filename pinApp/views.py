# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pinApp.forms import SimpleForm

global counter
counter = 0
another = 0
length = 0
myList = []
intList = []

def index(request):
	#return HttpResponse("Hello World!")
	myForm = SimpleForm(request.POST or None)

	global context
	context = {"form":myForm}
	if request.POST.get('submit') == 'submit':
		print('Submit clicked')

	if myForm.is_valid():
		length = (int)(myForm.cleaned_data.get("length"))
		myList = request.POST.getlist("options")

		for num in myList:
			temp = (int)(num)
			intList.append(temp)
		
		#print(myList)
		#first = (int)(myList[0]*length)
		#last = (int)(myList[len(myList)-1]*length)
		
		context = {'form':myForm,'length':length, 'myList':myList}

	return render(request,"home.html",context)

# Create your views here.
