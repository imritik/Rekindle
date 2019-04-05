from django import forms
from .models import Gov

class GovForm(forms.ModelForm):
	class Meta:
		model = Gov
		fields =[
		"Name",
		"Department",
		"Policy",
		]