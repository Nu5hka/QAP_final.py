from tests.config import url


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

