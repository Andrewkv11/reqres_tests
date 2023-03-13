from base.custom_requests import CustomRequest
import pytest
from base.assertions import Assertions
from base.schemas import UsersList, UserSingle


class TestGetUsers:

    @pytest.mark.parametrize('page', [1, 2])
    def test_get_list_users(self, page):
        params = {
            'page': page
        }
        response = CustomRequest.get('/users', params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UsersList)
        Assertions.assert_response_values(response, params, ['page'])

    def test_get_single_user(self):
        response = CustomRequest.get('/users/2')
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, UserSingle)

    def test_get_single_user_not_found(self):
        response = CustomRequest.get('/users/23')
        Assertions.assert_code_status(response, 404)

