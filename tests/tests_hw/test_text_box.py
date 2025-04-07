from pages.text_box import TextBox

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Test')
    text_box.current_address.send_keys('TestTestTest')
    text_box.btn_submit.click_force()
    displayed_name_text = text_box.displayed_name.get_text()
    displayed_address_text = text_box.displayed_current_address.get_text()
    assert displayed_name_text == 'Name:Test'
    assert displayed_address_text == 'Current Address :TestTestTest'