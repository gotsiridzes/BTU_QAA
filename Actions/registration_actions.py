from Locators.registration_locators import Registration_Locators

registration_locator = Registration_Locators()


def click_create_an_account_button():
    registration_locator.create_an_account_button.click()