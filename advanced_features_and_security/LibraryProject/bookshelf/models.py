from django.db import models
from django.contrib.auth.models import AbstarctUser

# Create your models here.
Class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=100),
    publication_year = models.DateField(), 

    def __str__(self):
        return self.title
    
# Additional information (Using AbstractUser)
Class CustomUser(AbstarctUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.username