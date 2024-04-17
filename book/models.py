from django.db import models


class RoomType(models.Model):
	description = models.CharField(max_length=20)
	supplement = models.IntegerField()

	def __str__(self):
		return self.description

class Status(models.Model):
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.status



class Registration(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	room = models.ForeignKey(RoomType, on_delete=models.CASCADE)
	notes = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name

