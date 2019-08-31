# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pinApp.forms import SimpleForm

myList = []
length = 0
another = 0
global counter
counter = 0
stringList = []
intList = []
values = []

def method(a,l):
	if a[l:l+1] in myList:
		#global counter
		counter = counter + 1

	if counter == length:
		global another
		another += 1
		values.append(a)

def index(request):
	#return HttpResponse("Hello World!")
	myForm = SimpleForm(request.POST or None)

	if request.POST.get('submit') == 'submit':
		print('Submit clicked')

	if myForm.is_valid():
		length = (int)(myForm.cleaned_data.get("length"))
		myList = request.POST.getlist("options")
		
		stringList = myList.copy()

		for a in myList:
			temp = (int)(a)
			intList.append(temp)
		#print(myList)
		first = (int)(myList[0]*length)
		last = (int)(myList[len(myList)-1]*length)

		for i in range(first,last+1):
			str_x = str(i)
			global counter
			counter = counter - counter
			for m in range(length):
				if method(str_x,m):
					continue

	context = {'form':myForm, 'length':length,'values':values}

	return render(request,"home.html",context)

# Create your views here.
