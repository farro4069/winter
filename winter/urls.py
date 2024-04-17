from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from book.views import index, RegisterView, VolunteerView, registrations, registration, RegistrationUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('volunteer/', VolunteerView.as_view(), name='volunteer'),
    path('registrations/', registrations, name='registrations'),
    path('registrations/<int:pk>/', registration, name='registration'),
    path('registrations/<int:pk>/update', RegistrationUpdateView.as_view(), name='update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


