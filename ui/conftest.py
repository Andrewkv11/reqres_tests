import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.main_page import MainPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://reqres.in/')
    driver.maximize_window()
    yield driver
    driver.quit()


# def buttons():
#     main_page = MainPage(driver)
#     buttons_list = main_page.buttons_list()
#     return buttons_list


# @pytest.fixture(params=buttons(driver))
# def fixt_buttons(request):
#     return request.param
