from base.custom_requests import CustomRequest
from base.assertions import Assertions
from base.schemas import UserLogin, UserLoginUnsuccessful


class TestUserLogin:

    def test_user_login_successful(self):
        user_credentials = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = CustomRequest.post('/login', data=user_credentials)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UserLogin)

    def test_user_login_unsuccessful(self):
        user_credentials = {
            "email": "peter@klaven"
        }
        response = CustomRequest.post('/login', data=user_credentials)
        Assertions.assert_code_status(response, 400)
        Assertions.validate_response_body(response, UserLoginUnsuccessful)
