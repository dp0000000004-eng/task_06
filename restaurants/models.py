from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class Book(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    guest_count = models.IntegerField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.guest_count} {self.message}"
