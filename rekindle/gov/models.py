from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Gov(models.Model):
	Name = models.CharField(max_length=120)
	Policyname = models.CharField(max_length=1200, default='0000000')
	Department = models.CharField(max_length = 100)
	Policy= models.CharField(max_length = 500)
	Policyid = models.IntegerField(default=0)
	def __str__(self):
		return self.Name

