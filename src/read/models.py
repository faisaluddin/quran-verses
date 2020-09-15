from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
