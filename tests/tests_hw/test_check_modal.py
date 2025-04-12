from pages.modal_dialogs import ModalDialogs
import pytest

def test_check_modal(browser):
    page_modal = ModalDialogs(browser)

    try:
        page_modal.visit()
    except Exception as e:
        pytest.skip(f"Страница недоступна: {e}")
        return

    assert page_modal.btn_small_modal.exist()
    assert page_modal.btn_large_modal.exist()
    page_modal.btn_small_modal.click()
    assert page_modal.modal_dialog.exist()
    page_modal.close_small.click()
    page_modal.btn_large_modal.click()
    assert page_modal.modal_dialog.exist()
    page_modal.close_large.click()
