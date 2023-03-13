from base.custom_requests import CustomRequest
from base.assertions import Assertions
from base.schemas import UserRegister, UserRegisterUnsuccessful


class TestUserRegister:

    def test_user_register_successful(self):
        user_credentials = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = CustomRequest.post('/register', data=user_credentials)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UserRegister)

    def test_user_register_unsuccessful(self):
        user_credentials = {
            "email": "eve.holt@reqres.in",
        }
        response = CustomRequest.post('/register', data=user_credentials)
        Assertions.assert_code_status(response, 400)
        Assertions.validate_response_body(response, UserRegisterUnsuccessful)
