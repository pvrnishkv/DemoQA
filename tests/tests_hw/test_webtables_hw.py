from pages.webtables_page import Webtables
import time

def test_webtables_1(browser):
    webtabkes_page = Webtables(browser)

    webtabkes_page.visit()
    assert webtabkes_page.btn_add.exist()
    webtabkes_page.btn_add.click()
    assert not webtabkes_page.btn_submit.click()
    assert webtabkes_page.modal_dialog.exist()
    webtabkes_page.f_name.send_keys('Tester')
    webtabkes_page.l_name.send_keys('Testerovitch')
    webtabkes_page.email.send_keys('123@mail.ru')
    webtabkes_page.age.send_keys('30')
    webtabkes_page.salary.send_keys('50000')
    webtabkes_page.department.send_keys('QA')
    webtabkes_page.btn_submit.click()
    assert not webtabkes_page.modal_dialog.exist()
    assert not webtabkes_page.entry_4.get_text() == ''
    webtabkes_page.pen_4.click()
    webtabkes_page.modal_dialog.exist()
    webtabkes_page.f_name.clear()
    time.sleep(2)
    webtabkes_page.f_name.send_keys('Toster')
    webtabkes_page.btn_submit.click()
    time.sleep(2)
    assert webtabkes_page.tab_4_1.get_text() == 'Toster'
    webtabkes_page.del_4.click()
    assert not webtabkes_page.entry_4.get_text() == ''

def test_webtables_2(browser):
    webtabkes_page = Webtables(browser)

    webtabkes_page.visit()
    webtabkes_page.rows.scroll_to_element()
    webtabkes_page.rows.click()
    webtabkes_page.rows_5.click()
    assert not webtabkes_page.btn_previous.click()
    assert not webtabkes_page.btn_next.click()
    assert webtabkes_page.btn_previous.get_dom_attribute('disabled')
    assert webtabkes_page.btn_next.get_dom_attribute('disabled')
    webtabkes_page.btn_add.click()
    webtabkes_page.f_name.send_keys('1')
    webtabkes_page.l_name.send_keys('1')
    webtabkes_page.email.send_keys('123@mail.ru')
    webtabkes_page.age.send_keys('1')
    webtabkes_page.salary.send_keys('1')
    webtabkes_page.department.send_keys('1')
    webtabkes_page.btn_submit.click()
    webtabkes_page.btn_add.click()
    webtabkes_page.f_name.send_keys('2')
    webtabkes_page.l_name.send_keys('2')
    webtabkes_page.email.send_keys('123@mail.ru')
    webtabkes_page.age.send_keys('2')
    webtabkes_page.salary.send_keys('2')
    webtabkes_page.department.send_keys('2')
    webtabkes_page.btn_submit.click()
    webtabkes_page.btn_add.click()
    webtabkes_page.f_name.send_keys('3')
    webtabkes_page.l_name.send_keys('3')
    webtabkes_page.email.send_keys('123@mail.ru')
    webtabkes_page.age.send_keys('3')
    webtabkes_page.salary.send_keys('3')
    webtabkes_page.department.send_keys('3')
    webtabkes_page.btn_submit.click()
    assert webtabkes_page.total_page.get_text() == '2'
    webtabkes_page.btn_next.click()
    assert webtabkes_page.page.get_dom_attribute('value') == '2'
    webtabkes_page.btn_previous.click()
    assert webtabkes_page.page.get_dom_attribute('value') == '1'
