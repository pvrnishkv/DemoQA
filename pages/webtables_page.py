from pages.base_page import BasePage
from components.components import WebElement

class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'span[title="Delete"]')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.f_name = WebElement(driver, '#firstName')
        self.l_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.entry_4 = WebElement(driver,'#app .web-tables-wrapper .rt-tbody > div:nth-child(2) > div > div')
        self.pen_4 = WebElement(driver, '#edit-record-4')
        self.del_4 = WebElement(driver, '#delete-record-4')
        self.tab_4_1 = WebElement(driver, '.web-tables-wrapper .rt-tbody > div:nth-child(4) > div > div:nth-child(1)')

        self.rows = WebElement(driver, '.select-wrap.-pageSizeOptions > select')
        self.rows_5 = WebElement(driver, '.web-tables-wrapper .pagination-bottom .select-wrap.-pageSizeOptions select option:nth-child(1)')
        self.btn_previous = WebElement(driver, '.-previous > button')
        self.btn_next = WebElement(driver, '.-next > button')
        self.total_page = WebElement(driver, '.-pageInfo > span')
        self.page = WebElement(driver, '#app .web-tables-wrapper .-pageInfo input[type=number]')

        self.col_f_name = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(1)')
        self.col_l_name = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(2)')
        self.col_age = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(3)')
        self.col_email = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(4)')
        self.col_salary = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(5)')
        self.col_department = WebElement(driver, '.web-tables-wrapper .ReactTable .rt-th:nth-child(6)')
