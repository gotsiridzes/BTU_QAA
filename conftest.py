from selenium import webdriver


class DriverSetUp:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    # driver.implicitly_wait(10)
