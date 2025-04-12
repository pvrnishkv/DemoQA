from pages.slider_page import SliderPage
from selenium.webdriver.common.keys import Keys

def test_slider(browser):
    slider_page = SliderPage(browser)

    slider_page.visit()
    assert slider_page.slider.exist()
    assert slider_page.inp.exist()
    while not slider_page.inp.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)
    assert slider_page.inp.get_dom_attribute('value') == '50'