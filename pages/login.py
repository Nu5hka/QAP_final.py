class LogPage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_email(self):
        return self.driver.find_element_by_xpath("//input[@name='login']")

    def get_password(self):
        return self.driver.find_element_by_xpath("//input[@name='password']")

    def get_log(self):
        return self.driver.find_element_by_xpath("//input[@value='Войти']")

    def get_myorder(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Мой профиль')]")

    def get_logerror(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),"
                                                 "'Неправильный email или пароль')]")
