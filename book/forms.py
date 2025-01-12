from django import forms
from django.forms import ModelForm
from .models import Registration


class RegistrationForm(ModelForm):
	class Meta:
		model = Registration
		fields = "__all__"

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	content = forms.CharField(max_length=400, widget=forms.Textarea)

	class Meta:
		fields = '__all__'
