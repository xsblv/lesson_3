from selene import browser, be, have

def test_search_failure(open_browser):
    browser.element('[name="text"]').should(be.blank).type('8e0c7987-b7d1-4cd1-bb05-2456e97384cb').press_enter()
    browser.element('.x-secondary.x-secondary-color').should(have.text('Не нашли нужного?'))