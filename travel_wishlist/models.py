from django.db import models

# Create your models here.

# this is a model much similar using peewee and this is for a visited and name of the place
class Place(models.Model): # define our db structure
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited? {self.visited}'
    




    
