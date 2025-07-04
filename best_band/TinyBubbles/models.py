from django.db import models
from django.contrib.auth.models import User

class TourDate(models.Model):
    date = models.DateField()
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    tickets_available = models.IntegerField(default=100)
    
    def __str__(self):
        return f"{self.date} - {self.venue}, {self.location}"

class FanMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.user.username}"