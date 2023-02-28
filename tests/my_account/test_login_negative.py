import pytest
from QAtest.src.pages.MyAccountSignetOut import MyAccountSignetOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        print("********")
        print("TEST LOGIN NON EXISTING")
        print("********")

        my_account = MyAccountSignetOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('cfhkkoii')
        my_account.input_login_password('fsgwhiuwy')
        my_account.click_login_button()

        # expected_err = 'Error: The username  is not registered on this site. If you are unsure of your username, try your email address instead.'
        # my_account.wait_until_error_is_displayed(expected_err)