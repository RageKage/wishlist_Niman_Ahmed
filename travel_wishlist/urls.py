from django.urls import path
from . import views

# routing

urlpatterns = [ 
    path('', views.place_list, name='place_list'), # by default this is the home page
    path('about/', views.about, name='about'),
    path('visited', views.places_visited, name="places_visited"), # this is the visited page url
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'), # to update a non visited place to visited

]