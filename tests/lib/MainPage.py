import os
import sys

this_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(this_dir, '..', '..', 'testlib', 'TestUtils'))
sys.path.append(os.path.join(this_dir, '..', '..', 'testlib', 'PageObjects'))

from ActionsPage import ActionsPage

class MainPage(ActionsPage):

    def __init__(self, driver, server):
        super(MainPage, self).__init__(driver, server)

    def _validate_page(self):
        # validate Main page is displaying a 'Home' tab
        # REVISIT
        pass

    def locate_search_input_area(self):
        input_locator = "//input[@title='Search']"
        input_area_element = self.find_element_by_xpath(input_locator,
                                                        "search input area")
        return input_area_element

    def search(self, search_input_area_element, text_to_search):
        self.enter_text(search_input_area_element, text_to_search)
