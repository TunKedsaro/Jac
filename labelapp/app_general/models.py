from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    tag  = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.name} {self.tag}"