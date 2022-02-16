from django.db import models

# Create your models here.

class Studenttxt(models.Model):
    q_txt = models.CharField(max_length=200,
     default='One night—it was on the twentieth of March, 1888—I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street')
     