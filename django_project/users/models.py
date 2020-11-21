from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customers(models.Model):
	Contact = models.IntegerField()
	Address = models.CharField(max_length = 69)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
