from playwright.sync_api import sync_playwright, expect, Page
import Buttons
from Buttons import Button
import inputs

page: Page

def get_page(playwright):

    global page
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demoqa.com/buttons')
    return browser

def check_if_the_output_is_good(btn, action):

    global page

    button = Button(btn)
    button.action(action)

    expect(button.get_button_message_locator()).to_be_visible()




def run(playwright):

    global page
    browser = get_page(playwright)
    Buttons.page = page

    for btn, action in inputs.input1.items():
        check_if_the_output_is_good(btn, action)

    page.wait_for_timeout(2000)


    browser.close()

with sync_playwright() as playwright:
    run(playwright)

