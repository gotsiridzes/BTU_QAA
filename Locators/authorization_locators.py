from selenium.webdriver.common.by import By
from conftest import DriverSetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = DriverSetUp.driverLogin
wait = WebDriverWait(driver, 10)


class Authorization_Locators:
    email_input = driver.find_element(By.ID, 'email')
    login_button = driver.find_element(By.CSS_SELECTOR, ".action.login.primary")
    password_input = wait.until(EC.visibility_of_element_located((By.ID, 'pass')))

    def login_button_success_message(self):
        try:
            success_message = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span")
            return success_message.text
        except Exception as e:
            return "No such element"

    def login_button_error_message_message(self):
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".message-error.error.message")
            return error_message.text
        except Exception as e:
            return "No such element"
