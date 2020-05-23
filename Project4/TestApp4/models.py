from django.db import models
# Create your models here.

class Employee(models.Model):
    Eno = models.IntegerField()
    Esal = models.FloatField()
    Ename = models.CharField(max_length=50)
    Eadd = models.CharField(max_length=50)

    def __str__(self):
        return self.Ename # Instead of employee object use this Function to display the required field.

