from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=10000)
    body = models.CharField(max_length=10000)
    def __str__(self):
        return str(self.name)
        
    