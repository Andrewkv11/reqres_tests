import json
from environment import ENV_URL
from ui.locators.main_page_locators import MainPageLocators
from ui.pages.base_page import BasePage
from base.custom_requests import CustomRequest


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_button(self, button):
        self.element_is_clickable(button).click()

    def parse_status_code(self):
        status_code = self.element_is_visible(self.locators.RESPONSE_CODE)
        return status_code.text

    def parse_response_body(self):
        response_body = self.element_is_visible(self.locators.RESPONSE_BODY)
        return response_body.text

    def parse_request_body(self):
        request_body = self.element_is_visible(self.locators.REQUEST_BODY)
        return request_body

    def api_response(self, button):
        button = self.element_is_clickable(button)
        button_method = button.get_attribute("data-http")
        button_url = button.find_element('xpath', self.locators.BUTTON_URL).get_attribute('href').replace(ENV_URL, '')
        if button_method == 'get':
            return CustomRequest.get(button_url)
        if button_method == 'delete':
            return CustomRequest.delete(button_url)
        request_body = json.loads(self.parse_request_body().text)
        if button_method == 'post':
            return CustomRequest.post(button_url, data=request_body)
        if button_method == 'put':
            return CustomRequest.put(button_url, data=request_body)
        if button_method == 'patch':
            return CustomRequest.patch(button_url, data=request_body)

