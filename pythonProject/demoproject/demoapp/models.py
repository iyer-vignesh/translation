from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# # Create your models here.
class folder(models.Model):
    upload = models.FileField(upload_to='Desktop/')

    def __str__(self):
        return str(self.upload) if self.upload else ''

        