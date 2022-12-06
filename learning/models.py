from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
    