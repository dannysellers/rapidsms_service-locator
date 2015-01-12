from django import forms
# from models import LocationType


class AddEntityForm(forms.Form):
	coordinates = forms.CharField(max_length = 200, required = True)
	name = forms.CharField(max_length = 100, required = True)
	# type = forms.ChoiceField(required = True, choices = tuple(enumerate(LocationType.objects.all())))
	type = forms.CharField(required = True)