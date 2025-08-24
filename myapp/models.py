from django.db import models

# Create your models here.
class record(models.Model):
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    city=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name