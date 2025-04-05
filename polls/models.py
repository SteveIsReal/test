from django.db import models

# Create your models here.
class User(models.Model):
	phone = models.IntegerField()
	bottle = models.IntegerField(default=0)

