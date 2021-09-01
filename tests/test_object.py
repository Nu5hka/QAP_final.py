from pages.base_page import BasePage
from pages.own_page import OwnPage
from pages.strollers_page import StrollersPage
from pages.car_seats_page import CarPage
from pages.login import LogPage
from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.config import email, passw, catalog, phone, menu, product, quantity, \
    category_sp, category_str, category_car, category_room, category_mat, \
    subcat_shoes, subcat_book, nameslider, devconditions
import time


# Загрузка главой страницы
def test_visit(driver):
    base_page = BasePage(driver)
    base_page.visit()
    assert base_page.get_log().is_displayed


# Проверка авторизации
def test_log(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    base_page.get_log().click()
    login_page = LogPage(driver)
    login_page.get_email().send_keys(email)
    login_page.get_password().send_keys(passw)
    login_page.get_log().click()
    assert login_page.get_myorder().is_displayed


# Соответствие меню каталога БТ
def test_catalog_menu(driver):
    base_page = BasePage(driver)
    base_page.visit()
    catalog_menu = base_page.get_catalog_menu()
    for i in range(len(catalog_menu)):
        assert catalog_menu[i].text == catalog[i]


# Соответствие меню БТ
def test_topmenu(driver):
    base_page = BasePage(driver)
    base_page.visit()
    topmenu = base_page.get_menu()
    top = topmenu[0].text.split(' ')
    for i in range(len(menu)):
        assert top[i] == menu[i]


##

# Проверка поиска
def test_search_cat(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.search().send_keys(product)
    base_page.search_run_button().click()
    a = base_page.products_titles().text.split(' ')
    assert a[1] == quantity


##

# Проверка поиска для авторизованного
def test_searchlog_cat(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    test_log(driver)
    base_page.search().send_keys(product)
    base_page.search_run_button().click()
    a = base_page.products_titles().text.split(' ')
    assert a[1] == quantity


##


# Соответствие категорий сопственного производства БТ прямой вход
def test_catown(driver):
    category_page = OwnPage(driver)
    category_page.categori_visit()
    category = category_page.get_categories()
    a = category[0].text.split('\n')
    for i in range(len(a)):
        assert a[i] == category_sp[i]


# Соответствие категории коляски БТ прямой вход
def test_catstr(driver):
    category_page = StrollersPage(driver)
    category_page.categori_visit()
    category = category_page.get_categori()
    a = category[0].text.split('\n')
    for i in range(len(a)):
        assert a[i] == category_str[i]


# Соответствие категории автокресла БТ прямой вход
def test_catcar(driver):
    category_page = CarPage(driver)
    category_page.categori_visit()
    category = category_page.get_categori()
    a = category[0].text.split('\n')
    for i in range(len(a)):
        assert a[i] == category_car[i]


# Соответствие категории детская комната БТ вход через главную страницу
def test_catroom(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_room().click()
    category = base_page.get_categories()
    a = category[0].text.split('\n')
    for i in range(len(a)):
        assert a[i] == category_room[i]


# Соответствие категории матрасы БТ для авторизованного
def test_catmattress(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    test_log(driver)
    base_page.get_mattress().click()
    category = base_page.get_categories()
    a = category[0].text.split('\n')
    for i in range(len(a)):
        assert a[i] == category_mat[i]


# Соответствие подкатегории детская обувь БТ вход через главную страницу
def test_subcat_shoes(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_clothershoes().click()
    base_page.get_shoes().click()
    category = base_page.get_categories()
    a = category[0].text.split('\n')
    del a[0]
    for i in range(len(subcat_shoes)):
        assert a[i] == subcat_shoes[i]


# Соответствие подкатегории книги детские БТ для авторизованного
def test_subcat_toybicycle(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    test_log(driver)
    base_page.get_toybicycle().click()
    base_page.get_book().click()
    category = base_page.get_categories()
    a = category[0].text.split('\n')
    del a[:5]
    for i in range(len(subcat_book)):
        assert a[i] == subcat_book[i]


# Проверка главного баннера
def test_slider(driver):
    base_page = BasePage(driver)
    base_page.visit()
    assert base_page.get_slider().is_displayed


# Проверка прехода с главного баннера на нужную страницу
def test_sliderclick(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_sliderclick().click()
    assert base_page.get_nameslider().text == nameslider


##

# Проверка акционного баннера для зарегистрированного
def test_bansale(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    test_log(driver)
    base_page.get_logo().click()
    assert base_page.get_bansale().is_displayed


# Проверка карты на странице магазинов
def test_shopmap(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_shops().click()
    assert base_page.get_maps().is_displayed


# Соответствие кнопок условий на странице доставки
def test_delcon(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_del().click()
    a = base_page.get_conditions().text.split('\n')
    conditions = []
    for i in range(len(a)):
        if a[i] != '':
            conditions.append(a[i])
    for j in range(len(conditions)):
        assert conditions[j] == devconditions[j]


# Переход по кнопке корзина для не авторизованного
def test_basket(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_cart().click()
    assert base_page.get_cart().is_displayed


# добавление суммы товара из поиска в значек корзинки на главной для не авторизованного
def test_basket_addsearch(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.search().send_keys(product)
    base_page.search_run_button().click()
    base_page.get_butbuy()[0].click()
    time.sleep(5)
    a = base_page.get_cart_total()
    assert a.text != "0 P"


# добавление суммы товара из каталога в значек корзинки на главной для авторизованного
def test_basket_addcat(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'toTop')))
    test_log(driver)
    base_page.get_toybicycle().click()
    time.sleep(5)
    base_page.get_book().click()
    time.sleep(5)
    base_page.get_butbuy()[1].click()
    time.sleep(5)
    a = base_page.get_cart_total()
    assert a.text != "0 P"


# соответские суммы заказа нескольких товаров из акции с суммой в значке корзинки на главной
# для неавторизованного
def test_basket_sumsale(driver):
    base_page = BasePage(driver)
    base_page.visit()
    base_page.get_sliderclick().click()
    base_page.get_butbuy()[0].click()
    time.sleep(5)
    base_page.get_butbuy()[1].click()
    time.sleep(5)
    a = base_page.get_cart_total().text.replace("Р", "")
    b = base_page.get_price()[0].text.replace("Р", "")
    c = base_page.get_price()[1].text.replace("Р", "")
    assert float(a.replace(" ", "")) == float(b.replace(" ", "")) + float(c.replace(" ", ""))
    return a


# наличие выбранных товаров в корзине не авторизованный
def test_basket_add(driver):
    test_basket_addsearch(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_cart().is_displayed


##

# Проверка соответствие суммы выбранных товаров с суммой в корзине
# неавторизованный
def test_basket_total(driver):
    total = test_basket_sumsale(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_cart_total().text.replace("Р", "") == total


# наличие способа доставки в корзине для авторизованного
def test_basket_del(driver):
    test_basket_addcat(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_del().is_displayed


##


# наличие способа оплаты в корзине для авторизованного
def test_basket_pay(driver):
    test_basket_addcat(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_pay().is_displayed


##

# наличие окна комментариев в корзине для авторизованного
def test_basket_comments(driver):
    test_basket_addcat(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_comments().is_displayed
##

# проверка полей в контактной информации при оформлении заказа для неавторизованного
def test_basket_info(driver):
    test_basket_sumsale(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    assert basket_page.get_firstname().is_displayed
    assert basket_page.get_email().is_displayed
    assert basket_page.get_phone().is_displayed
    assert basket_page.get_lastname().is_displayed
    assert basket_page.get_address().is_displayed
##

# Удаление товаров из корзины для авторизванного
def test_basket_delete(driver):
    test_basket_addcat(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    basket_page.get_delete().click()
    assert basket_page.get_null_basket().is_displayed
##

# Кнопка быстрого оформления для не авторизванного
def test_basket_quickbut(driver):
    test_basket_addsearch(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    basket_page.scroll()
    basket_page.get_quick_but().click()
    assert basket_page.get_dialog().is_displayed
##

# Кнопка оформления заказа для авторизованного
# Очистить корзину пользователя
def test_basket_order(driver):
    test_basket_addcat(driver)
    basket_page = BasketPage(driver)
    basket_page.visit()
    basket_page.scroll()
    basket_page.get_order().send_keys(phone)
    assert basket_page.get_order()
##
# pytest -vv -s -k "_basket_order"
