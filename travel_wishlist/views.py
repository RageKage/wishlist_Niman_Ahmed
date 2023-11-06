from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import newPlaceForm, DateInput, TripReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
# similar to services

@login_required
def place_list(request):
    return render(request, 'travel_wishlist/wishlist.html')

# get all of places in the db

@login_required
def place_list(request):
    
    if request.method == 'POST': # this is to check if the request is a post request
        form = newPlaceForm(request.POST) # this is to create a form object from the post data
        place = form.save(commit=False) 
        
        place.user = request.user # this is to link the place to the user
        
        if form.is_valid(): # this is to check if the form is valid
            place.save() # this is to save the form data to the database
            return redirect('place_list') # this is to redirect to the place list page
    
    
    
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by(
        'name')  # this is to get all the places from the database
    new_Place_Form = newPlaceForm()
    # this is to pass the places to the template
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_Place_Form})

@login_required
def places_visited(request): 
    visited = Place.objects.filter(visited=True) # this is to get all the places visited from the database
    return render(request, 'travel_wishlist/visited.html', {'visited': visited}) # this is to pass the visited places to the template

@login_required
def place_was_visited(request, place_pk): # this is to mark a place as visited
    if request.method == 'POST':
        # this is to get the place from the database
        # place = Place.objects.get(pk=place_pk) #this is to get the matching primary key from the database
        place = get_object_or_404(Place, pk=place_pk) # this is to get the matching primary key from the database and if it does not exist it will return a 404 error
        if place.user == request.user: # this is to check if the user is the same as the user who created the place
            
            place.visited = True
            place.save()  # this is to save the place to the database
        else: 
            return HttpResponseForbidden() 
    return redirect('place_list')  # this is to redirect to the place list page when the place is visited instead of taking them to the places visited page


@login_required
def place_infos(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    
    if place.user != request.user: # checks if the user is the same as the user who created the place
        return HttpResponseForbidden()
    
    if request.method == 'POST': # POST request to update the place
        form = TripReviewForm(request.POST, request.FILES, instance=place) # create a form instance from the data in the request
        
        if form.is_valid(): # check if the form is valid compared to the model we created (the database fields)
            form.save()
            messages.info(request, 'Trip information updated!')
        else: 
            messages.error(request, form.errors) # error message if the form is not valid
        
        return redirect('place_infos', place_pk=place_pk)
            
    else:
        if place.visited: # check if the place is visited
            review_form = TripReviewForm(instance=place) # create the form with the data from the database
            return render(request, 'travel_wishlist/place_info.html', {'place': place, 'review_form': review_form}) # return the place and the form to the template 
        else: 
            return render(request, 'travel_wishlist/place_info.html', {'place': place})





@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    
    if request.method == 'POST':
        if place.user == request.user:
            place.delete()
            return redirect('place_list')
        else:
            return HttpResponseForbidden()
        

 

@login_required
def about(request): 
    author = 'Niman Ahmed' 
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about}) # this is to pass the author and about to the template