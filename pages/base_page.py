from tests.config import url


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_catalog_menu(self):
        return self.driver.find_elements_by_xpath("//img[@class='header_catalog-menu']")

    def get_log(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Вход')]")

    def get_menu(self):
        return self.driver.find_elements_by_xpath("//*[@id='navtop']")

    def search(self):
        return self.driver.find_element_by_xpath("//input[@placeholder='Введите запрос...']")

    def search_run_button(self):
        return self.driver.find_element_by_xpath("//div[@type='button']")

    def products_titles(self):
        return self.driver.find_element_by_xpath("//div[@class='searchpro__page-description "
                                                 "js-searchpro__page-description']")

    def get_room(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Детская комната')]")

    def get_categories(self):
        return self.driver.find_elements_by_xpath("//ul[@class='pc_cw_categories-menu']")

    def get_mattress(self):
        return self.driver.find_element_by_xpath("//a[@class='cat585']")

    def get_clothershoes(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Одежда и обувь детская')]")

    def get_shoes(self):
        return self.driver.find_element_by_xpath("//a[contains(text(),'Обувь детская')]")

    def get_toybicycle(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Велосипеды, игрушки, коврики')]")

    def get_book(self):
        return self.driver.find_element_by_xpath("//a[contains(text(),'Книги детские')]")

    def get_slider(self):
        return self.driver.find_element_by_id('slider-37')

    def get_sliderclick(self):
        return self.driver.find_element_by_xpath("//a[@href='https://antoshkaspb.ru/category/aktsiya-1705-300621/']")

    def get_nameslider(self):
        return self.driver.find_element_by_xpath("//h1[@class='category-name']")

    def get_bansale(self):
        return self.driver.find_element_by_id('slider-39')

    def get_logo(self):
        return self.driver.find_element_by_xpath("//img[@class='logoanimate3']")

    def get_shops(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Магазины')]")

    def get_maps(self):
        return self.driver.find_element_by_xpath("//*[@style='margin-top:20px;']")

    def get_del(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Доставка')]")

    def get_conditions(self):
        return self.driver.find_element_by_id('example2')

    def get_cart(self):
        return self.driver.find_element_by_id('cart')

    def get_yourcart(self):
        return self.driver.find_element_by_xpath("//h1[contains(text(),'Корзина')]")

    def get_butbuy(self):
        return self.driver.find_elements_by_xpath("//input[@type='submit']")

    def get_cart_total(self):
        return self.driver.find_element_by_xpath("//strong[@class='cart-total']")

    def get_price(self):
        return self.driver.find_elements_by_css_selector(".price.nowrap")

    def get_img(self):
        return self.driver.find_elements_by_css_selector('img[src*="data"]')
