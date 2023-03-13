import pytest
from base.assertions import Assertions
from ui.locators.main_page_locators import MainPageLocators
from ui.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize('button', MainPageLocators().BUTTONS_LIST)
    def test_endpoints(self, driver, button):
        main_page = MainPage(driver)
        main_page.click_button(button)
        api_response = main_page.api_response(button)
        output_status_code = main_page.parse_status_code()
        output_response_body = main_page.parse_response_body()
        Assertions.assert_code_status(api_response, int(output_status_code))
        Assertions.assert_response_body(api_response, output_response_body)
