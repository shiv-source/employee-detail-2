from django.db import models

# Create your models here.

class Emaployee(models.Model):
    employee_Id= models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    salary= models.IntegerField()
    details=models.TextField()
    developer=models.BooleanField(default=False)
    business_dev=models.BooleanField(default=False)

    def __str__(self):
        return self.name