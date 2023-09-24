from selene import browser, have, be


def test_successful_login():
    # GIVEN
    browser.open('https://demowebshop.tricentis.com/')

    # WHEN
    browser.element('.ico-login').click()

    # AND
    browser.element('#Email').type('marharyta.shcherbakova@gmail.com')
    browser.element('#Password').type('1234567890')
    browser.element('.login-button').click()

    # THEN
    browser.element('.header .account').should(have.text('marharyta.shcherbakova@gmail.com'))
    browser.element('.ico-logout').should(be.visible)

    def test_logout():
        browser.open('https://demowebshop.tricentis.com/')
        browser.element('.header .account').should(have.text('marharyta.shcherbakova@gmail.com'))
        browser.element('.ico-logout').should(be.visible)
        browser.element('.logout-button').click()




test_successful_login()
