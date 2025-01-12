from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from book.views import (index, route, RegisterView, 
    VolunteerView, registrations, registrations_room, detailedregistrations, 
    registration, RegistrationUpdateView, important, ContactView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('route/', route, name='route'),
    path('register/', RegisterView.as_view(), name='register'),
    path('volunteer/', VolunteerView.as_view(), name='volunteer'),
    path('registrations/', registrations, name='registrations'),
    path('rooms/', registrations_room, name='rooms'),
    path('detail/', detailedregistrations, name='detail'),
    path('registrations/<int:pk>/', registration, name='registration'),
    path('registrations/<int:pk>/update', RegistrationUpdateView.as_view(), name='update'),
    path('important/', important, name='important'),
    path('contact/', ContactView.as_view(), name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


