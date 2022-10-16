from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	location = models.CharField(max_length=100)
	salary = models.DecimalField(max_digits=15, decimal_places=2)
	def __str__(self):
		return self.name

class TestTable(models.Model):
	height = models.IntegerField()
	width = models.IntegerField()
	


