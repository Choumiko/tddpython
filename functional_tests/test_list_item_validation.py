from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #enter on empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        #error message item cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        
        #works with text
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        # second blank
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        #warning
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('1: Make tea')