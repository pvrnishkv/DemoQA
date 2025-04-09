from pages.webtables_page import Webtables
import time

def test_webtables(browser):
    webtabkes_page = Webtables(browser)

    webtabkes_page.visit()
    assert not webtabkes_page.no_data.exist()

    while webtabkes_page.btn_delete_row.exist():
        webtabkes_page.btn_delete_row.click()

    time.sleep(2)
    assert webtabkes_page.no_data.exist()