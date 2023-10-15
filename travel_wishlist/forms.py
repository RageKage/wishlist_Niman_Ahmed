from django import forms
from .models import Place

# this is the form to add a new place
class newPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited' )
        