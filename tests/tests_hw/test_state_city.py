from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys
import time

def test_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_state_Uttar_Pradesh.click()
    form_page.btn_city.scroll_to_element()
    form_page.btn_city.click()
    form_page.btn_city_Merrut.click()
    time.sleep(2)

def test_state_city_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('Uttar Pradesh')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)
    form_page.inp_city.send_keys('Merrut')
    form_page.inp_city.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_city_3(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)
    form_page.btn_city.click()
    form_page.inp_city.send_keys(Keys.PAGE_DOWN)
    form_page.inp_city.send_keys(Keys.ENTER)
    time.sleep(2)