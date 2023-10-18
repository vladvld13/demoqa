from playwright.sync_api import sync_playwright, expect, Page

test1 = {
    'name': 'Andrei',
    'email': 'andrei@gmail.com',
    'CurrentAddress': 'Bucharest',
    'PermanentAddress': 'Bucharest'
}


class TextBox:

    def __init__(self, field, value):

        self.field = field
        self.value = value

    def check_field(self):

        if self.field == 'name':
            self.field = 'Full Name'
        elif self.field == 'email':
            self.field = 'name@example.com'
        elif self.field == 'CurrentAddress':
            self.field = 'Current Address'
        elif self.field == 'PermanentAddress':
            self.field = '#permanentAddress-wrapper #permanentAddress'
        else:
            raise InvalidInputError('Invalid textbox')
        return self.field

    def check_value(self):
        invalid_characters = '!@#$%^&*()_+=-1234567890{[]}\|:;/?,.'
        if self.field == 'Full Name':
            for character in invalid_characters:
                if character in self.value:
                    raise InvalidInputError("not a valid name")

        elif self.field == 'name@example.com':
            for character in '@.':
                if character not in self.value or self.value.count('@') > 1 or len(self.value) < 4:
                    raise InvalidInputError("not a valid email")
        return self.value


class InvalidInputError(Exception):

    def __init__(self, name):
        self.name = name


def get_page(playwright):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demoqa.com/text-box')
    return page, browser


def test_output_contains_text(page: Page, value) -> None:
    out_locator = page.locator("id=output")
    expect(out_locator).to_contain_text(value)


def run(playwright):
    page, browser = get_page(playwright)

    for field, value in test1.items():
        try:
            tb = TextBox(field, value)
            if tb.field == 'PermanentAddress':
                page.locator(tb.check_field()).fill(tb.check_value())
            else:
                page.get_by_placeholder(tb.check_field()).fill(tb.check_value())
        except InvalidInputError as error:
            print(error)

    page.get_by_role("button", name="Submit").click()

    out_locator = page.locator("id=output")

    for value in test1.values():
        test_output_contains_text(page, value)

    # test_output_contains_text(page, 'abc123')   #this test should fail

    out = out_locator.inner_text()
    print(out.split('\n\n'))

    browser.close()


with sync_playwright() as playwright:
    run(playwright)

