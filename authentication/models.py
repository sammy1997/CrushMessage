from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message_text = models.TextField(null = True)

	def __str__(self):
		return self.message_text
