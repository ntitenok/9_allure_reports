
from selene import browser
from selene import by, be, have
def test_github_simple():

    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure - example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.text('Issue for HW qa.guru')).click()

    browser.element('.gh-header-title').should(have.text('Issue for HW qa.guru'))
