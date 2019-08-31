# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pinApp.forms import SimpleForm

global counter
global another
length = 0
myList = []
intList = []

def index(request):
	#return HttpResponse("Hello World!")
	myForm = SimpleForm(request.POST or None)

	counter = 0
	pinCount = 0
	global context
	context = {"form":myForm}
	if request.POST.get('submit') == 'submit':
		print('Submit clicked')

	if myForm.is_valid():
		length = (int)(myForm.cleaned_data.get("length"))
		myList = request.POST.getlist("options")
		myOtherList = []

		first = (int)(myList[0]*length)
		last = (int)(myList[len(myList)-1]*length)

		index = 0;
		for pin in range(first,last+1):
			str_pin = str(pin).zfill(length)
			counter -= counter

			for digit in range(length):
				if str_pin[digit:digit+1] in myList:
					counter = counter + 1

				if counter == length:
					
					print(str_pin)
					myOtherList.append(str_pin);
					pinCount += 1


		'''for num in myList:
			temp = (int)(num)
			intList.append(temp)'''


		
		#print(myList)
		#first = (int)(myList[0]*length)
		#last = (int)(myList[len(myList)-1]*length)
		
		context = {'form':myForm,'length':pinCount, 'myList':myOtherList}


	return render(request,"home.html",context)

# Create your views here.
