from django import forms
from .models import User1

class UserForm(forms.ModelForm):
	class Meta:
		model = User1
		fields = [

		"Name",
		"adhaar_no",
		"team_size",
		"address",
		"proposal",
		]

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	

	