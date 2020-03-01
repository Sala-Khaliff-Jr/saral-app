from django.db import models

# Create your models here.
class Registrations(models.Model):
    student_name = models.CharField(blank=False,null=False,max_length=30)
    college_name = models.CharField(blank=False,null=False,max_length=50)
    email_id = models.EmailField(unique=True)
    reg_id = models.CharField(unique=True,max_length=16)
    events = models.CharField(blank=False,null=False,max_length=300)
    total_cost = models.CharField(blank=False,null=False,max_length=10)
    
    def __str__(self):
        return self.student_name+" "+self.reg_id