from pages.accordian_page import AccordianPage
import time

def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert accordian_page.text_element.visible()
    accordian_page.text_element_head.click()
    time.sleep(2)
    assert not accordian_page.text_element.visible()

def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert not accordian_page.text_element_1.visible()
    assert not accordian_page.text_element_2.visible()
    assert not accordian_page.text_element_3.visible()