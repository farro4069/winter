from django.contrib import admin
from .models import Membership, Status, RoomType, Registration
# Register your models here.


admin.site.register(Membership)
admin.site.register(Status)
admin.site.register(RoomType)
admin.site.register(Registration)
