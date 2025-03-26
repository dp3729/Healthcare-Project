from django.db import models
from authentication_api.models import CustomUser

# Create your models here.

class Doctor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="doctors")  
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name