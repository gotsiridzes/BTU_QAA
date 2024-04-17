from selenium.webdriver.common.by import By
from conftest import DriverSetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = DriverSetUp.driver
wait = WebDriverWait(driver, 10)


class Registration_Locators:
    first_name_input = driver.find_element(By.ID, 'firstname')
    create_an_account_button = driver.find_element(By.CSS_SELECTOR, ".action.submit.primary")
    last_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'lastname')))
    email_input = driver.find_element(By.ID, 'email_address')
    password_input = driver.find_element(By.ID, 'password')
    password_confirm_input = driver.find_element(By.ID, 'password-confirmation')

    def create_an_account_button_success_message(self):
        try:
            success_message = driver.find_element(By.CSS_SELECTOR, ".message-success.success.message")
            return success_message.text
        except Exception as e:
            return "No such element"

    def create_an_account_button_account_already_exists_message(self):
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".message-error.error.message")
            return error_message.text
        except Exception as e:
            return "No such element"
