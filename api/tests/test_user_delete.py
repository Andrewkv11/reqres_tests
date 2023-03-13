from base.custom_requests import CustomRequest
from base.assertions import Assertions


class TestUserCreate:

    def test_user_delete(self):
        response = CustomRequest.delete('/users/2')
        Assertions.assert_code_status(response, 204)

