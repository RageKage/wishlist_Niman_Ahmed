from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import newPlaceForm

# Create your views here.

# this is the place list view

# similar to services


def place_list(request):
    return render(request, 'travel_wishlist/wishlist.html')

# get all of places in the db


def place_list(request):
    
    if request.method == 'POST': # this is to check if the request is a post request
        form = newPlaceForm(request.POST) # this is to create a form object from the post data
        place = form.save() 
        if form.is_valid(): # this is to check if the form is valid
            place.save() # this is to save the form data to the database
            return redirect('place_list') # this is to redirect to the place list page
    
    
    
    places = Place.objects.filter(visited=False).order_by(
        'name')  # this is to get all the places from the database
    new_Place_Form = newPlaceForm()
    # this is to pass the places to the template
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_Place_Form})



def about(request): 
    author = 'Niman Ahmed' 
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about}) # this is to pass the author and about to the template


def places_visited(request): 
    visited = Place.objects.filter(visited=True) # this is to get all the places visited from the database
    return render(request, 'travel_wishlist/visited.html', {'visited': visited}) # this is to pass the visited places to the template


def place_was_visited(request, place_pk): # this is to mark a place as visited
    if request.method == 'POST':
        # this is to get the place from the database
        # place = Place.objects.get(pk=place_pk) #this is to get the matching primary key from the database
        place = get_object_or_404(Place, pk=place_pk) # this is to get the matching primary key from the database and if it does not exist it will return a 404 error
        place.visited = True
        place.save()  # this is to save the place to the database
    return redirect('place_list')  # this is to redirect to the place list page when the place is visited instead of taking them to the places visited page
 

