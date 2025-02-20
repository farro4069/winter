from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView
from .models import Membership, RoomType, Status, Registration, Price, Inclusion
from .forms import RegistrationForm, ContactForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def index(request):
	sharing = get_object_or_404(Price, item='Sharing')
	ride = get_object_or_404(Price, item='Ride only')
	auscycling = get_object_or_404(Price, item='AusCycling')
	inclusions = Inclusion.objects.filter(included = True)

	context = {
		'sharing': sharing,
		'ride': ride,
		'auscycling': auscycling,
		'inclusions': inclusions,
	}

	return render(request, 'index.html', context)


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
			rooms = RoomType.objects.all()
			context = {
				'registered': registered,
				'rooms': rooms,
			}

			invoice_html = render_to_string('invoice.html', context)
			invoice_plain = strip_tags(invoice_html)

			msg = EmailMultiAlternatives(
				'Winter Warmer Registration',
				invoice_plain,
				settings.EMAIL_HOST_USER,
				[registered.email],
			)
			msg.attach_alternative(invoice_html, "text/html")
			msg.send()

			return render(request, 'confirm.html', context)

		else:
			message = 'Please fix the errors'
			details = request.POST

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

def registrations_room(request):
	registrations = Registration.objects.all().order_by('name')
	context = {
		'registrations': registrations,
	}
	return render(request, 'registrations_room.html', context)

def registration(request, pk):
	registration = get_object_or_404(Registration, id = pk)
	context = {
		'registration': registration,
	}
	return render(request, 'registration.html', context)

def detailedregistrations(request):
	registrations = Registration.objects.all().order_by('id')
	context = {
		'registrations': registrations,
	}
	return render(request, 'detailedregistrations.html', context)

def important(request):
	solosupplement = get_object_or_404(Price, item='SoloSupplement')
	inclusions = Inclusion.objects.filter(included = False)
	ride = get_object_or_404(Price, item='Ride only')

	context = {
		'inclusions': inclusions,
		'ride': ride,
	}
	return render(request, 'important.html', context)

def route(request):
	context = {}
	return render(request, 'route.html', context)

class RegistrationUpdateView(UpdateView):
	model = Registration
	template_name = "registration_update.html"
	fields = ['name', 'email', 'membership', 'status', 'room', 'notes']
	success_url = '../'

class ContactView(View):
	def get(self, request):

		form = ContactForm()

		context = {
			'form': form,
		}

		return render(request, 'contact.html', context)

	def post(self, request):
		question = ContactForm(request.POST)

		if question.is_valid():
			
			name = question.cleaned_data["name"]
			email_from = question.cleaned_data["email"]
			content = question.cleaned_data["content"]
			subject = 'Winter Warmer Enquiry'

			context = {
				'name': name,
				'email_from': email_from,
				'subject': subject,
				'content': content,
			}

			question_html = render_to_string('question.html', context)
			question_plain = strip_tags(question_html)

			msg = EmailMultiAlternatives(
				subject,
				question_plain,
				email_from,
				[settings.EMAIL_HOST_USER],
				reply_to=[email_from,]
			)

			msg.attach_alternative(question_html, "text/html")
			msg.send()

			return render(request, 'contacted.html', context)

		else:
			message = 'Please fix the errors'
			details = request.POST

			context = {
				'form': question,
				'details': details,
				'message': message,
				}

			return render(request, 'contact.html', context, )




