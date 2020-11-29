from django.db import models

# Create your models here.

class Post(models.Model):
	Name= models.CharField(max_length=100)
	Location=models.TextField()
	#Cuisines=models.TextField()
	#PriceRange=models.TextField()
	#Ratings=models.TextField()
	
class Rest(models.Model):
	Name= models.CharField(max_length=100)
	Location=models.TextField()
	Cuisines=models.TextField()
	PriceRange=models.TextField()
	Ratings=models.TextField()

	def __str__(self):
		return self.Name 
