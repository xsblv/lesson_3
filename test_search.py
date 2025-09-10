from selene import browser, be, have

def test_search_success(open_browser):
    browser.element('[name="text"]').should(be.blank).type('bmw ultramarine').press_enter()
    browser.element('.c-search-item__body').should(have.text('BMW 4 series (F32) Ultramarine'))
