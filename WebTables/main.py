from playwright.sync_api import sync_playwright, expect, Page
import RegistrationField
from RegistrationField import RegistrationField as registrationField
from Error import InputNotSavedError, InvalidCommand, RowNotDeleted
import input

page: Page

rows = "10"

def get_page(playwright):

    global page
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demoqa.com/webtables')
    return browser

def form_execute(command):

    """
    This function performs the action for the form: Submit or Close
    If Submit is chosen, the input will be saved in the table. If the command is 'Close', it won't be saved.
    Any command which is not "Submit" or "Close" will raise an error.
    """
    if command != 'Submit' and command != 'Close':
        raise InvalidCommand("Invalid form command: You should select Submit or Close")

    page.get_by_role("button", name=command).click()


def table_output():

    """
    Verify each row in the table and if that row is not empty, save it in out_list.
    This function returns a list of lists representing the rows in the web table.

    """

    out_list = []
    for row in range(int(rows)):
        if len(page.get_by_role("rowgroup").nth(row).inner_text().split()) > 0:
            out_list.append(page.get_by_role("rowgroup").nth(row).inner_text().split())

    return out_list

def add_element_to_table_and_check(input_data):

    """
    Press 'add' button from the webpage, a form will be opened;
    Search each field from that form in the input dictionary keys
    Fill the fields with the coresponding values
    Press Submit or Close
    Check if the input is saved in the table
    return error if 'Submit' is selected and the input is not saved
    """

    page.get_by_role('button', name="Add").click()

    for key,value in input_data[0].items():
        field = registrationField(key)
        field.fill_registration_form(value)

    form_execute(input_data[1])
    if not is_input_saved_in_table(input_data[0]) and input_data[1] == 'Submit':
        raise InputNotSavedError('The input is not saved')
    elif input_data[1] == 'Close':
        print('Data not saved')


def is_input_saved_in_table(input_dict: dict):
    """
    Verify if the values from the input dictionary are saved in the table
    """
    output_list = table_output()
    val_list = [value for value in input_dict.values()]
    return val_list in output_list

def delete_element_from_table_and_check(fullname):

    """
    Search the table output for the line which contains name and surname,
    get the email (which is unique for each line),
    locate the line you want to delete by the email and delete it.

    """

    name = fullname.split()[0]
    surname = fullname.split()[1]

    for data_list in table_output():
        if name in data_list and surname in data_list:
            mail = data_list[3]

    row_to_be_deleted = page.get_by_text(mail, exact=True).locator('xpath=..').get_by_text(surname, exact=True).locator('xpath=..')
    deleted_row_text = row_to_be_deleted.inner_text().split()
    row_to_be_deleted.locator('.action-buttons').get_by_title('Delete').click()

    if deleted_row_text in table_output():
        raise RowNotDeleted('The row is not deleted')





def run(playwright):

    global page
    browser = get_page(playwright)
    RegistrationField.page = page

    add_element_to_table_and_check(input.input1)


    delete_element_from_table_and_check("Cierra Vega")




    page.wait_for_timeout(3000)



    browser.close()


with sync_playwright() as playwright:
    run(playwright)


