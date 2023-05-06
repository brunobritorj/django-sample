from django.db import models
from djongo import models as djongo_models

class Author(djongo_models.Model):
    _id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
