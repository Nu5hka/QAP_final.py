import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    print(request.fspath)
    driver = webdriver.Chrome(f"{path[:path.find('tests')]}tests/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
