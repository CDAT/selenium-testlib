import os
import sys
import time

this_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(this_dir, '..', 'testlib', 'TestUtils'))
sys.path.append(os.path.join(this_dir, '..', 'testlib', 'PageObjects'))
sys.path.append(os.path.join(this_dir, 'lib'))

from BaseTestCase import BaseTestCase
from MainPage import MainPage

class TestOpenBrowser(BaseTestCase):

    def test_google_search(self):
        main_page = MainPage(self.driver, "https://www.google.com")

        input_area_element = main_page.locate_search_input_area()
        time.sleep(3)
        main_page.search(input_area_element, "google scholar")

        
