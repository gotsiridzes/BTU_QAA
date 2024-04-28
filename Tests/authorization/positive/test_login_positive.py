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
    authorization_locator.email_input.send_keys('Saba@Gotsiridze1.Com')
    authorization_locator.password_input.send_keys('Pa$$w0rd!@#')

    click_login_button()

    expected_success_message = "Welcome, saba gotsiridze!"
    actual_success_message = authorization_locator.create_an_account_button_success_message()

    assert expected_success_message in actual_success_message

    DriverSetUp.driver.quit()

