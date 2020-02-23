from django.db import models

# Create your models here.
class Registrations(models.Model):
    student_name = models.CharField(blank=False,null=False,max_length=30)
    email_id = models.EmailField(unique=True)