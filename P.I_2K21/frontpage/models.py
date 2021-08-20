from django.db import models

# Create your models here.

class users(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"