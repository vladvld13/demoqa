from playwright.sync_api import sync_playwright, expect, Page
page: Page

class RegistrationField:

    def __init__(self, name):
        self.name = name
        self.placeholder = 'name@example.com' if self.name == 'Email' else self.name

    def fill_registration_form(self,value):
        global page
        page.get_by_placeholder(self.placeholder).fill(value)
        page.wait_for_timeout(500)