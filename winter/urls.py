from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from book.views import index, RegisterView, VolunteerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('volunteer/', VolunteerView.as_view(), name='volunteer'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


