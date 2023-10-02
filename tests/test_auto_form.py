from selene.support.shared import browser
from selene import be, have, by

def test_fill_form():
    browser.open("https://demoqa.com/automation-practice-form")

    browser.element('#firstName').click().type('Rita')
    browser.element('#lastName').click().type('Shch')
    browser.element('#userEmail').click().type('test@test.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').click().type('780080080804')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react - datepicker__year - select').click().element(by.text('2000'))
    browser.element('.react-datepicker__month-select').click().element(by.text('August'))
    browser.element('.react-datepicker__week').click().element(by.text('26'))
