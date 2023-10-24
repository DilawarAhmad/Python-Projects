from django.db import models

# Create your models here.
class Geeks(models.Model):
    title=models.CharField(max_length=23)
    description=models.TextField(max_length=40)

    def __str__(self):
        return self.title