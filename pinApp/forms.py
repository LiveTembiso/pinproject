
from django import forms

class SimpleForm(forms.Form):
	length = forms.DecimalField(min_value = 0, label="Pin Length")
	NUMBERS = [("0","0"),("1","1"),(2,"2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9")]
	options = forms.MultipleChoiceField(label = "Digit Options", choices=NUMBERS, widget=forms.CheckboxSelectMultiple())