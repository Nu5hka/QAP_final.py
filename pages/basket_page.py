from tests.config import urlbasket


class BasketPage(object):
    _locator = '//*[@value="Быстрое оформление заказа"]'

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(urlbasket)

    def get_cart(self):
        return self.driver.find_element_by_xpath("//div[@class='cartOS__cart']")

    def get_cart_total(self):
        return self.driver.find_element_by_xpath("//span[@class='cartOS__cartTotal']")

    def get_del(self):
        return self.driver.find_element_by_xpath("//div[@class='cartOS__shipping']")

    def get_pay(self):
        return self.driver.find_element_by_xpath("//div[@class='cartOS__payment']")

    def get_comments(self):
        return self.driver.find_element_by_xpath("//div[@class='cartOS__confirmation']")

    def get_firstname(self):
        return self.driver.find_element_by_css_selector(".wa-field.wa-field-firstname")

    def get_email(self):
        return self.driver.find_element_by_css_selector(".wa-field.wa-field-email")

    def get_phone(self):
        return self.driver.find_element_by_css_selector(".wa-field.wa-field-phone")

    def get_lastname(self):
        return self.driver.find_element_by_css_selector(".wa-field.wa-field-lastname")

    def get_address(self):
        return self.driver.find_element_by_css_selector(".wa-field.wa-field-address")

    def get_delete(self):
        return self.driver.find_element_by_xpath("//span[@class='cartOS__cartDelete']")

    def get_null_basket(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Ваша корзина пуста')]")

    def get_order(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Оформить заказ')]")

    def get_quick_but(self):
        return self.driver.find_element_by_xpath("//*[@value='Быстрое оформление заказа']")

    def get_dialog(self):
        return self.driver.find_element_by_xpath("//div[@class='dialog-content-indent']")

    def scroll(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def error_phone(self):
        return self.driver.find_element_by_xpath("//input[@class='error']")
