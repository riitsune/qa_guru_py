from selene.support.shared import browser
from selene import be, have

browser.open('https://demoqa.com/text-box')

browser.element('#userName').click().type('Rita')
browser.element('#userEmail').click().type('test@test.com')
browser.element('#currentAddress').click().type('somewhere in the world')
browser.element('#permanentAddress').click().type('Russia')
browser.element('#submit').click()

browser.element('#output').should(be.visible)
browser.element('#name').should(have.text('Rita'))
browser.element('#email').should(have.text('test@test.com'))
browser.element('#output #currentAddress').should(have.text('somewhere in the world'))
browser.element('#output #permanentAddress').should(have.text('Russia'))
