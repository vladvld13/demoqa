from playwright.sync_api import sync_playwright, expect, Page
import RadioButton
from RadioButton import RadioButton as radiobutton
from ClickError import ClickError as clickerror

page: Page

def get_page(playwright):

    global page
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demoqa.com/radio-button')
    return browser


def check_output(button: radiobutton):

    button.click_button()
    expect(page.locator('.mt-3')).to_have_text(f"You have selected {button.name}")

def is_button_disabled(button: radiobutton):

    button_class = button.get_button_class()

    return 'disabled' in button_class




def run(playwright):

    global page
    browser = get_page(playwright)
    RadioButton.page= page

    button = radiobutton("Yes")

    if (is_button_disabled(button)):
        raise clickerror("Button disabled")

    check_output(button)

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
