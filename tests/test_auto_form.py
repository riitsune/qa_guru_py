from selene.support.shared import browser
from selene import have, command, by
import os

def test_fill_form():
    browser.open("https://demoqa.com/automation-practice-form")

    browser.element('#firstName').click().type('Rita')
    browser.element('#lastName').click().type('Shch')
    browser.element('#userEmail').click().type('test@test.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').click().type('78008008080')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(by.text('2000')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(by.text('August')).click()
    browser.element(by.text('26')).click()


    browser.element('#subjectsInput').click().type('Math').press_enter()
    # browser.with_(timeout=browser.config.timeout * 3).element('[for="hobbies-checkbox-2"]').click()
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/image.jpg'))
    browser.element('#currentAddress').click().type("Saints-Petersburg, Sizova av.,9")
    browser.element('#state').click()
    browser.element(by.text('Uttar Pradesh')).click()
    browser.element('#city').click()
    browser.element(by.text('Agra')).click()

    browser.element('#submit').execute_script('element.click()')

    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'Rita Shch',
        'test@test.com',
        'Female',
        '7800800808',
        '26 August,2000',
        'Maths',
        '',
        'image.jpg',
        'Saints-Petersburg, Sizova av.,9',
        'Uttar Pradesh Agra'
    ))


