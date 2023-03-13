from base.custom_requests import CustomRequest
from base.assertions import Assertions
from base.schemas import UserUpdate, UserUpdatePart


class TestUserUpdate:

    def test_user_update(self):
        user_data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = CustomRequest.put('/users/2', data=user_data)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UserUpdate)
        Assertions.assert_response_values(response, user_data, ["name", "job"])

    def test_user_update_part(self):
        user_data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = CustomRequest.patch('/users/2', data=user_data)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UserUpdatePart)
        Assertions.assert_response_values(response, user_data, ["name", "job"])
