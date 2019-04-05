from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User1(models.Model):
	Name = models.CharField(max_length=120)
	title = models.CharField(max_length=120 )
	adhaar_no= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999999999)])
	team_size = models.IntegerField(validators=[MaxValueValidator(999)])
	address = models.CharField(max_length = 100)
	proposal = models.CharField(max_length = 500)
	def __str__(self):
		return self.Name