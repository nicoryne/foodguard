from django.db import models
from django.utils import timezone

# Classes within users/models.py
#   1. User


# User
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11)
    date_of_birth = models.DateTimeField()
    
    @property
    def age(self):
        if self.date_of_birth is None:
            return None
        
        today = timezone.now().date()
        age = int (
            today.year
            - (self.date_of_birth.year)
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
    
        return age
    
    def __str__(self):
        return (
            f"User ID: {self.user_id}\n"
            f"Name: {self.lname}, {self.fname}\n"
            f"Email: {self.email}\n"
            f"Phone #: {self.phone_number}\n"
            f"Birthdate: {self.date_of_birth}\n"
            f"Age: {self.age}"
        )