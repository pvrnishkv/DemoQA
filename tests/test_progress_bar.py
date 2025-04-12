from pages.progress_bar import ProgressBar
import time

def test_slider(browser):
    progress_bar = ProgressBar(browser)

    progress_bar.visit()
    time.sleep(2)
    progress_bar.button.click()

    while True:
        if progress_bar.progress.get_dom_attribute('aria-valuenow') == '51':
            progress_bar.button.click()
            break

    time.sleep(2)