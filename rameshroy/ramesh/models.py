from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100)

    class Meta:
        db_table = 'login'  # This tells Django to use the existing 'login' table
