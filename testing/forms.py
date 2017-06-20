#class BookForm(forms.ModelForm):
#   class = Book

from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from testing.models import Form1,Form3

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username',max_length=30)
	first_name = forms.CharField(label='First Name', max_length=15)
	last_name = forms.CharField(label='Last Name', max_length=15)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password',
		widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm Password',
		widget= forms.PasswordInput())
	List = [(1, 'Waste Generator/Waste Processor'), (2, 'Government Official'),]
	item_list = ( ('User', tuple(List)),)
	itemsField = forms.ChoiceField(label = 'SingUp as',choices = tuple(item_list))
	docfile = forms.FileField(label='ID Document',
		widget=forms.FileInput())

	#def is_WGWP()



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
	
class EditProfileForm(forms.ModelForm):

	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label="Last Name")

	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class Form1_form(forms.ModelForm):
	class Meta:
		model = Form1
		site_clear = forms.FileField(widget=forms.FileInput())
		fields = ['address','fax','nodal', 'authorization', 'site_clear','env_clear','consent','agreement',	'investment','quant_recycle','quant_treat','quant_dispose','util','method_dis',	'quant_leach','treatleach','measure','safety','details','no_sw','quant_sw','details_sw','op_sw','landfill_sw','poll','date','info',]
		#def save_model(self, request, obj, form, change):
		#	obj.user = request.user
		#	obj.save()
		
class Form3_form(forms.ModelForm):
	class Meta:
		model = Form3
		ww_waste = forms.FileField(widget=forms.FileInput())
		#widget=forms.FileInput())
		fields = ['city','pop','area', 'name_loc', 'fax_loc','name_op','name_off','no_hh',	'no_nr','no_e','quant_sw','es_sw','quant_d','per_cap',	'procc_sw','dis_sw','p_bins','p_ins','p_street','p_sw','p_seg','p_d2d','p_hh','p_nr','p_d','p_motor','p_hcart','p_other','ww_waste',]

