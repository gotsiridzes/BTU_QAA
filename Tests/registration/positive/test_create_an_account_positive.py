import traceback
from Actions.registration_actions import click_create_an_account_button
from Locators.registration_locators import Registration_Locators
from conftest import DriverSetUp
from qaseio.pytest import qase


registration_locator = Registration_Locators()


@qase.id(2)
@qase.title('Create an account test')
@qase.fields(
    ("severity", "critical"),
    ("priority", "high"),
    ("layer", "unit"),
    ("description", "Try to register new user on webpage")
)
def test_create_an_account_positive():
    registration_locator.first_name_input.send_keys('Saba1')
    registration_locator.last_name_input.send_keys('Gotsiridze')
    registration_locator.email_input.send_keys('Saba@Gotsiridze1.Com')
    registration_locator.password_input.send_keys('Pa$$w0rd!@#')
    registration_locator.password_confirm_input.send_keys('Pa$$w0rd!@#')

    click_create_an_account_button()

    expected_success_message = "Thank you for registering with Main Website Store."
    # expected_already_registered_message = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
    actual_success_message = registration_locator.create_an_account_button_success_message()
    # actual_account_already_exists_message = registration_locator.create_an_account_button_account_already_exists_message()

    assert expected_success_message in actual_success_message

    DriverSetUp.driver.quit()
