from django.db import models

# Create your models here.

class dict(models.Model):
    english=models.CharField(max_length=100)
    uzbek=models.CharField(max_length=100)

    def __str__(self):
        return self.english + '-' + self.uzbek