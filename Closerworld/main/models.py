from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    
    