from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_first_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')

        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.close_small = WebElement(driver, '#closeSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.close_large = WebElement(driver, '#closeLargeModal')