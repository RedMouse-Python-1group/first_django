# coding=utf-8

from django.db import models

# Create your models here.
class App (models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    enable = models.BooleanField(default=False)

    def get_absolute_url(self):
        return 'page/'+self.pk

    class Meta:
        verbose_name = "pizza"
        verbose_name_plural = 'The bunch of stuff'
