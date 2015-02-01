from django import forms
from models import Entity
from leaflet.forms.fields import PointField


class AddEntityForm(forms.Form):
	coordinates = forms.CharField(max_length = 200, required = True)
	name = forms.CharField(max_length = 100, required = True)
	type = forms.CharField(required = True)


class EntityForm(forms.ModelForm):
	location = PointField()

	class Meta:
		model = Entity
		fields = ('location', 'type', 'name')