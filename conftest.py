from selenium import webdriver


class DriverSetUp:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    
    driverLogin = webdriver.Chrome()
    driverLogin.maximize_window()
    driverLogin.get("https://magento.softwaretestingboard.com/customer/account/login/")
    # driver.implicitly_wait(10)
