from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase): 

    # setUpClass and tearDownClass are used to start and stop the Selenium WebDriver
    @classmethod 
    def setUpClass(cls): 
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    
    # once they are set uo then we can write our tests
    def test_title_on_home_page(self): 
        self.selenium.get(self.live_server_url)# this is the url of the server
        self.assertIn('Travel wish list', self.selenium.title) # now we can use the selenium object to get the title of the page
        

class AddNewPlaceTest(LiveServerTestCase):
    
    fixtures = ['test_places']
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    
    def test_add_new_place(self):
        self.selenium.get(self.live_server_url)
        input_name = self.selenium.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        
        add_button = self.selenium.find_element_by_id('add-new-place')
        add_button.click()
        
        denver = self.selenium.find_element_by_id('place-name-5')
        self.assertEqual('Denver', denver.text) 
        
        # The test failed be AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'
        
        self.assertIn('Denver', self.selenium.page_source)
        
        self.assertIn('New York', self.selenium.page_source)
        
        self.assertIn('Moab', self.selenium.page_source)
        
        
        
        
        
        
        

