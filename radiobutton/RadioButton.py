from playwright.sync_api import sync_playwright, expect, Page
from ClickError import ClickError as clickerror

page: Page

class RadioButton:

    def __init__(self, name):
        self.name = name

    def get_button_location(self):
        global page

        return page.get_by_text(self.name)

    def get_button_class(self):

        return self.get_button_location().locator('xpath=..').get_attribute("class")

    def click_button(self):

        if self.name != 'No':

            self.get_button_location().click()

        else:
            raise clickerror(f'"{self.name}" button is not clickable')

        page.wait_for_timeout(2000)