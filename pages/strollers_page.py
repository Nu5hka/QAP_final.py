from tests.config import urlstr


class StrollersPage(object):
    def __init__(self, driver):
        self.driver = driver

    def categori_visit(self):
        self.driver.get(urlstr)

    def get_categori(self):
        return self.driver.find_elements_by_xpath("//ul[@class='pc_cw_categories-menu']")