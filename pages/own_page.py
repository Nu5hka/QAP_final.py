from tests.config import urlsp


class OwnPage(object):
    def __init__(self, driver):
        self.driver = driver

    def categori_visit(self):
        self.driver.get(urlsp)

    def get_categories(self):
        return self.driver.find_elements_by_xpath("//ul[@class='pc_cw_categories-menu']")

