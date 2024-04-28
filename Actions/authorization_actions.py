from Locators.authorization_locators import Authorization_Locators

authorization_locator = Authorization_Locators()


def click_login_button():
    authorization_locator.login_button.click()