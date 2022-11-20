from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    name = models.CharField(max_length=80)
    review = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review
