from selenium.webdriver.common.by import By


class MainPageLocators:
    RESPONSE_CODE = (By.CSS_SELECTOR, "span[data-key='response-code']")
    RESPONSE_BODY = (By.CSS_SELECTOR, "pre[data-key='output-response']")
    REQUEST_URI = (By.CSS_SELECTOR, "span[data-key='url']")
    BUTTON_URL = './/a'
    REQUEST_BODY = (By.CSS_SELECTOR, "pre[data-key='output-request']")
    BUTTONS_LIST = [
        (By.CSS_SELECTOR, "li[data-id='users']"),
        (By.CSS_SELECTOR, "li[data-id='users-single']"),
        (By.CSS_SELECTOR, "li[data-id='users-single-not-found']"),
        (By.CSS_SELECTOR, "li[data-id='unknown']"),
        (By.CSS_SELECTOR, "li[data-id='unknown-single']"),
        (By.CSS_SELECTOR, "li[data-id='unknown-single-not-found']"),
        (By.CSS_SELECTOR, "li[data-id='post']"),
        (By.CSS_SELECTOR, "li[data-id='put']"),
        (By.CSS_SELECTOR, "li[data-id='patch']"),
        (By.CSS_SELECTOR, "li[data-id='delete']"),
        (By.CSS_SELECTOR, "li[data-id='register-successful']"),
        (By.CSS_SELECTOR, "li[data-id='register-unsuccessful']"),
        (By.CSS_SELECTOR, "li[data-id='login-successful']"),
        (By.CSS_SELECTOR, "li[data-id='login-unsuccessful']"),
        (By.CSS_SELECTOR, "li[data-id='delay']"),
    ]






