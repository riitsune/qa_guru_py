from selene.support.shared import browser
from selene import be, have


def test1(browser_conf):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test2(browser_conf):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gfdghdsghdmjthndgfxn').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("По данному запросу нет никаких результатов")