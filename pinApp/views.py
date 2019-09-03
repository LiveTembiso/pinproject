# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pinApp.forms import SimpleForm

def index(request):
	#return HttpResponse("Hello World!")
	myForm = SimpleForm(request.POST or None)
	submit = request.POST.get('submit')

	global counter
	length = 0
	numOptions = []
	pins = []
	counter = 0
	pinCount = 0
	global context
	context = {"form":myForm}

	if myForm.is_valid():
		length = (int)(myForm.cleaned_data.get("length"))
		numOptions = request.POST.getlist("options")

		first = (int)(numOptions[0]*length)
		last = (int)(numOptions[len(numOptions)-1]*length)

		index = 0;
		for pin in range(first,last+1):
			str_pin = str(pin).zfill(length)
			counter -= counter

			for digit in range(length):
				if str_pin[digit:digit+1] in numOptions:
					counter = counter + 1

				if counter == length:
					
					pins.append(str_pin);
					pinCount += 1
		
		context = {'form':myForm,'length':pinCount, 'options':pins, 'submit':submit}

	return render(request,"home.html",context)

# Create your views here.