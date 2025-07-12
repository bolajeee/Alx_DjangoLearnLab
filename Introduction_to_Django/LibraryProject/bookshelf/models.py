from django.db import models

# Create your models here.
Class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=100),
    publication_year = models.DateField(), 

    def __str__(self):
        return self.title