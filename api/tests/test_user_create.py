from base.custom_requests import CustomRequest
from base.assertions import Assertions
from base.schemas import UserCreate


class TestUserCreate:

    def test_user_create(self):
        user_data = {
            "name": "morpheus",
            "job": "leader"
        }
        response = CustomRequest.post('/users', data=user_data)
        Assertions.assert_code_status(response, 201)
        Assertions.validate_response_body(response, UserCreate)
        Assertions.assert_response_values(response, user_data, ["name", "job"])
