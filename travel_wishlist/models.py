from django.db import models

from django.contrib.auth.models import User
# Create your models here.

# this is a model much similar using peewee and this is for a visited and name of the place
class Place(models.Model): # define our db structure
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE) # this is to link the place to the user
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)
    

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo' # return the photo url if there is a photo else return no photo
        notes_str = self.notes[100:] if self.notes else 'no notes' # return the first 100 characters of the notes if there are notes else return no notes
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Notes: {self.notes} Photo: {photo_str}'
    




    
