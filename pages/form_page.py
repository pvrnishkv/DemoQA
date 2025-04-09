from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver,'#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver,'#submit')
        self.modal_dialog = WebElement(driver,'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver,'#closeLargeModal')
        self.hobbies_check_1 = WebElement(driver, '#hobbies-checkbox-1')
        self.address = WebElement(driver, '#currentAddress')
        self.user_form = WebElement(driver, '#userForm')

        self.btn_state = WebElement(driver, '#state')
        self.btn_state_Uttar_Pradesh = WebElement(driver, "//*[contains(text(), 'Uttar Pradesh')]", 'xpath')
        self.inp_state = WebElement(driver, '#react-select-3-input')

        self.btn_city = WebElement(driver, '#city')
        self.btn_city_Merrut = WebElement(driver, "//*[contains(text(), 'Merrut')]", 'xpath')
        self.inp_city = WebElement(driver, '#react-select-4-input')
