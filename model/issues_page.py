from selene import browser
from selene import by, have
import allure



class Issue_page:
    @allure.step('Открыть страницу {page}')
    def open_page(self, page):
        browser.open(page)
    @allure.step('Перейти в репозиторий {repo}')
    def go_to_repo(self, repo):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type(repo).press_enter()
        browser.element(by.link_text(repo)).click()

    @allure.step('Открыть вопрос по проблеме {issue}')
    def go_to_issue(self, issue):
        browser.element('#issues-tab').click()
        browser.element(by.text(issue)).click()

    @allure.step('Проверить текст в заголовке {title}')
    def assert_tittle_text(self, title):
        browser.element('.gh-header-title').should(have.text(title))
