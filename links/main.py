from playwright.sync_api import sync_playwright, expect, Page, BrowserContext, Browser
import link
from link import Link, LocalLink

context: BrowserContext
browser: Browser
page: Page


def get_context(playwright):

    global browser, context

    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    context = browser.new_context()


def go_to_link(link):

    global page
    page = context.new_page()
    page.goto(link)

    return page


def check_link_to_a_new_page(link_name):

    lnk = Link(link_name)
    href = lnk.get_locator().get_attribute('href')
    lnk.get_locator().click()
    new_page = context.wait_for_event('page')
    new_page.wait_for_load_state()
    new_page_url = new_page.url
    return(new_page_url == href+'/')


def local_link(link_name):

    lnk = LocalLink(link_name)
    lnk.get_locator().click()
    return lnk.name in lnk.output()



def run(playwright):

    get_context(playwright)
    link.context = context
    initial_page = go_to_link('https://demoqa.com/links')
    page = initial_page
    link.page = page




    #print(page.locator('#created').get_attribute('href'))

    print(check_link_to_a_new_page('dynamicHome'))
    print(local_link('Created'))


    browser.close()


with sync_playwright() as playwright:
    run(playwright)

