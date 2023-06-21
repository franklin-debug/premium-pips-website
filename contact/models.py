from django.db import models

# Create your models here.
class Message(models.Model):
	name = models.CharField(max_length=50)
	mobile_no = models.IntegerField()
	email = models.EmailField()
	message_details =models.CharField(max_length=300)


	def __str__(self):
		return self.name

class Register(models.Model):
	name = models.CharField(max_length=50)
	mobile_no = models.IntegerField()
	email = models.EmailField()
	plan =models.CharField(max_length=300)


	def __str__(self):
		return self.name