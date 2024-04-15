from django.contrib import admin
from .models import Registration, Status, RoomType
# Register your models here.


admin.site.register(Registration)
admin.site.register(Status)
admin.site.register(RoomType)