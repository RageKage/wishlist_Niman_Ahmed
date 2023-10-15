from django.test import TestCase
from django.urls import reverse
from .models import Place

# Create your tests here.

class TestHomePage(TestCase):
    
    def test_home_page_shows_empty_list_message_for_empty_database(self): # Test the home page
        home_page_url = reverse('place_list') # Get the URL for the place_list view
        response = self.client.get(home_page_url)   # Get the home page
        self.assertTemplateUsed('travel_wishlist/wishlist.html') # Check the right template was used
        self.assertContains(response, 'No places added to the wishlist yet.') # Check for the response for the message
    
    

class TestWishList(TestCase): 
    
    fixtures = ['test_places'] # Load test data from test_places.json
    
    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list')) # 
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo') # Check for Tokyo
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco') # Check for San Francisco
        self.assertNotContains(response, 'Moab')
        
class TestVisitedMessage(TestCase):
    
    def test_visited_page_message(self):
        visited_page_url = reverse('places_visited')
        response = self.client.get(visited_page_url)
        self.assertTemplateUsed('travel_wishlist/visited.html')
        self.assertContains(response, "You haven't visited any places yet.")

        
        
class TestVisited(TestCase):
    
    fixtures = ['test_places']
    
    def test_visited_page_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')


class TestAddNewPlace(TestCase):
    
    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False}
        response = self.client.post(add_place_url, new_place_data, follow=True)
        
        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        
        # Check data was added to the database
        response_places = response.context['places']
        self.assertEqual(1, len(response_places))
        tokyo_from_response = response_places[0]
        
        tokyo_from_db = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_from_db, tokyo_from_response)
        
        
class TestVisitedPlace(TestCase):
    
    fixtures = ['test_places']
    
    def test_visit_place(self):
        # using pk to get the url for the place_was_visited view
        visited_place_url = reverse('place_was_visited', args=(2, )) 
        response = self.client.post(visited_place_url, follow=True) # follow=True to follow redirects
        
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html') # Check correct template was used
        
        self.assertNotContains(response, 'New York') # Check response doesn't contain New York
        
        self.assertContains(response, 'Tokyo') # Check response does contain Tokyo
        
        new_york_db = Place.objects.get(pk=2) # Get New York from the database again, to check it's now visited
        
        self.assertTrue(new_york_db.visited) # Check it's visited
        
    def test_non_existed_place(self):
        # using pk to get the url for the place_was_visited view but with a non existed pk
        visited_place_url = reverse('place_was_visited', args=(200, )) 
        response = self.client.post(visited_place_url, follow=True)
        
        self.assertEqual(404, response.status_code) # Check it's 404 not found
        