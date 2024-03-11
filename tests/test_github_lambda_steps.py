from selene import browser
from selene import by, have
import allure
from allure_commons.types import Severity

@allure.title('Тест Github lambda steps')
def test_github_lambda():
    allure.dynamic.tag('github')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Tест раздела Issues')
    allure.dynamic.story('Название раздела содержит текст Issue for HW qa.guru')
    allure.dynamic.link("https://github.com", name="Тест репозитория")

    with allure.step('Открыть Github'):
        browser.open('https://github.com')

    with allure.step('Перейти в репозиторий allure-example'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam / allure - example').press_enter()
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Проверить раздел Issue for HW qa.guru'):
        browser.element('#issues-tab').click()
        browser.element(by.text('Issue for HW qa.guru')).click()

    with allure.step('Проверить название раздела'):
        browser.element('.gh-header-title').should(have.text('Issue for HW qa.guru'))
