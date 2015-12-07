from django.db import models

# Create your models here.
class App (models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    enable = models.BooleanField(default=False)
