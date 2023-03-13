from base.custom_requests import CustomRequest
from base.assertions import Assertions
from base.schemas import UsersList, UserSingle


class TestDelay:

    def test_get_delay(self):
        params = {
            'delay': 3
        }
        response = CustomRequest.get('/users', params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UsersList)
