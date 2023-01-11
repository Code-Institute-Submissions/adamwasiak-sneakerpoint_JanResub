from django.db import models
from django.contrib.auth.models import User

# database model for reviews app


class Review(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.review)
