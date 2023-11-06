from django import forms
from .models import Place

# this is the form to add a new place
class newPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited' )
        

class DateInput(forms.DateInput):
    input_type = 'date'
    

class TripReviewForm(forms.ModelForm): 
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo') 
        widgets = {
            'date_visited': DateInput(),
        }