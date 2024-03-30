from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    # Add other fields like address, description, etc.
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    overall_rating = models.IntegerField(default=0)
    cleanliness_rating = models.IntegerField(default=0)
    staff_rating = models.IntegerField(default=0)
    amenities_rating = models.IntegerField(default=0)
    # comments = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by_manager = models.BooleanField(default=False)  # Indicates whether the review has been approved by a manager

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"  # Customize as needed

    class Meta:
        ordering = ['-created_at']  # Order reviews by creation date, newest first

class Rating(models.Model):
    ASPECT_CHOICES = (
        ('cleanliness', 'Cleanliness'),
        ('staff_friendliness', 'Staff Friendliness'),
        ('amenities', 'Amenities'),
        ('room_comfort', 'Room Comfort'),
        # Add other aspects
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    aspect = models.CharField(max_length=50, choices=ASPECT_CHOICES)
    stars = models.IntegerField(default=0)



from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    # Add other fields as needed

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    # Add other fields as needed
