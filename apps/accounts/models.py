from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
            - ((today.month, today.day) < 
              (self.date_of_birth.month, self.date_of_birth.day))
        )
    
        return age