from pages.webtables_page import Webtables

def test_webtables_1(browser):
    webtables_page = Webtables(browser)

    webtables_page.visit()
    webtables_page.col_f_name.click()
    assert 'sort-asc' in webtables_page.col_f_name.get_dom_attribute('class')
    webtables_page.col_l_name.click()
    assert 'sort-asc' in webtables_page.col_l_name.get_dom_attribute('class')
    webtables_page.col_age.click()
    assert 'sort-asc' in webtables_page.col_age.get_dom_attribute('class')
    webtables_page.col_email.click()
    assert 'sort-asc' in webtables_page.col_email.get_dom_attribute('class')
    webtables_page.col_salary.click()
    assert 'sort-asc' in webtables_page.col_salary.get_dom_attribute('class')
    webtables_page.col_department.click()
    assert 'sort-asc' in webtables_page.col_department.get_dom_attribute('class')

