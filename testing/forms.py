#class BookForm(forms.ModelForm):
#   class = Book

from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username',max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password',
		widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm Password',
		widget= forms.PasswordInput())

	#password match testing
	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
			raise forms.ValidationError('Passwords do not match')

	#username taken or not / username validity
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$',username):
			raise forms.ValidationError('Username can only contain letters, numbers and underscore')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username already exists. Please try a different one')
				