from playwright.sync_api import sync_playwright, expect, Page, BrowserContext, Browser
from Errors import InvalidLink

page: Page

class Link:
    def __init__(self, name):
        self.name = name

    def get_locator(self):

        valid_link_names = ['Home', 'Created', 'No Content',
                            'Moved', 'Bad Requests', 'Unauthorized',
                            'Forbidden', 'Not Found']

        if self.name == 'dynamicHome':
            return page.locator('#dynamicLink')

        elif self.name in valid_link_names:
            return page.get_by_role("link", name= self.name)

        else:
            raise InvalidLink('This link is not on the page')


class LocalLink(Link):

    def output(self):
        return page.locator('#linkResponse').inner_text()

    def is_it_a_local_link(self):

        if self.get_locator(page).get_attribute('href') == "javascript:void(0)":
            return True
        else:
            return False

