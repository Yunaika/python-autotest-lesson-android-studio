import allure
from python_autotest_lesson_android_studio import app
from selene import have, be
from allure_commons._allure import step
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


@allure.tag("Android")
@allure.label("owner", "JuliaMur")
@allure.story("Поиск в Википедии")
def test_wikipedia_search():
    with step('Open app'):
        app.given_opened()

    with step('Search text from the first page'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).tap()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Crime and punishment')

    with step('Opening 1 item in search list'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[0].click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_page_header_image')).should(be.visible)

    with step('Search text from inside page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_toolbar_button_search')).tap()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('2022')

    with step('Opening 2 item in search list'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[1].click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_page_header_image')).should(be.visible)
