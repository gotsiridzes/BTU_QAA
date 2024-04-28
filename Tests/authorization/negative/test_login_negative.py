import traceback
from Actions.authorization_actions import click_login_button
from Locators.authorization_locators import Authorization_Locators
from conftest import DriverSetUp
from qaseio.pytest import qase


authorization_locator = Authorization_Locators()


@qase.id(2)
@qase.title('Create an account test')
@qase.fields(
    ("severity", "critical"),
    ("priority", "high"),
    ("layer", "unit"),
    ("description", "Try to register new user on webpage")
)
def test_login_positive():
    authorization_locator.email_input.send_keys('a@b.ge')
    authorization_locator.password_input.send_keys('123')

    click_login_button()

    expected_negative_message = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    actual_negative_message = authorization_locator.login_button_error_message_message()

    assert expected_negative_message in actual_negative_message

    DriverSetUp.driver.quit()

