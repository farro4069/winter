from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView
from .models import Membership, RoomType, Status, Registration
from .forms import RegistrationForm

def index(request):
	return render(request, 'index.html')


class RegisterView(View):
	model = Registration

	def get(self, request):
		form = RegistrationForm()
		context = {
			'form': form,
		}
		return render(request, 'register.html', context)

	def post(self, request):
		register = RegistrationForm(request.POST)
		if register.is_valid():
			booking = register.save(commit = False)
			booking.save() 

			registered = Registration.objects.latest('id')

			context = {
				'registered': registered,
			}
			return render(request, 'confirm.html', context)

		else:
			message = 'Please fix the errors'
			details = request.POST
			print(details)
			context = {
				'form': register,
				'details': details,
				'message': message,
				}

			return render(request, 'register.html', context, )


class VolunteerView(View):
	def get(self, request):
		context = {
			
		}
		return render(request, 'volunteer.html', context)

def registrations(request):
	registrations = Registration.objects.all().order_by('name')
	context = {
		'registrations': registrations,
	}
	return render(request, 'registrations.html', context)

def registration(request, pk):
	registration = get_object_or_404(Registration, id = pk)
	context = {
		'registration': registration,
	}
	return render(request, 'registration.html', context)

def important(request):
	context = {}
	return render(request, 'important.html', context)

def route(request):
	context = {}
	return render(request, 'route.html', context)

class RegistrationUpdateView(UpdateView):
	model = Registration
	template_name = "registration_update.html"
	fields = ['name', 'email', 'membership', 'status', 'room', 'notes']
	success_url = '../'
