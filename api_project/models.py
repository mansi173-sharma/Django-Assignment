from django.db import models

# Create your models here.

class User(models.Model):
   id = models.BigAutoField(primary_key=True)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   company_name = models.CharField(max_length=100)
   age = models.PositiveIntegerField()
   city = models.CharField(max_length=20)
   state = models.CharField(max_length=20)
   zip = models.BigIntegerField()
   email = models.CharField(max_length=50)
   web = models.CharField(max_length=50)

