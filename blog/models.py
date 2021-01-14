from django.db import models
from datetime import date

# Create your models here.
class Blogs(models.Model):
    blogtitle = models.CharField(max_length=100)
    blogdescription = models.CharField(max_length=250)
    blogtext = models.CharField(max_length=2500)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.blogtitle