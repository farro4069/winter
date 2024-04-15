from django.forms import ModelForm
from .models import Registration


class RegistrationForm(ModelForm):
	class Meta:
		model = Registration
		fields = "__all__"

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)

