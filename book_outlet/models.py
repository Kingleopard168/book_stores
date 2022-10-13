from email.policy import default
from pickle import FALSE
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here .

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(sefe):
        return f"{sefe.title} ({sefe.rating})"