from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name
