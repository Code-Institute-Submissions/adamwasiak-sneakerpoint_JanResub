from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=80)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.review} by {self.name}"