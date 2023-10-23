from playwright.sync_api import sync_playwright, expect, Page
from Errors import InvalidButton

page: Page
class Button:

    def __init__(self, name):
        self.name = name


    def get_locator(self):

        if self.name == "Click Me":
            return page.get_by_role('button', name="Click Me", exact=True)
        elif self.name == "Double Click Me":
            return page.get_by_role('button', name="Double Click Me")
        elif self.name == "Right Click Me":
            return page.get_by_role('button', name="Right Click Me")
        else:
            raise InvalidButton("The selected button doesn't exist")

    def action(self, action_name):

        if action_name == 'Click':
            self.get_locator().click()
        elif action_name == 'Double Click':
            self.get_locator().dblclick()
        elif action_name == 'Right Click':
            self.get_locator().click(button='right')

    def get_button_message_locator(self):

        if self.name == "Click Me":
            return page.locator('#dynamicClickMessage')
        elif self.name == "Double Click Me":
            return page.locator('#doubleClickMessage')
        elif self.name == "Right Click Me":
            return page.locator('#rightClickMessage')


