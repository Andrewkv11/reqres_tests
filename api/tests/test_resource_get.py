from base.custom_requests import CustomRequest
import pytest
from base.assertions import Assertions
from base.schemas import ResourceList, ResourceSingle


class TestGetResource:

    @pytest.mark.parametrize('page', [1, 2])
    def test_get_list_resource(self, page):
        params = {
            'page': page
        }
        response = CustomRequest.get('/unknown', params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, ResourceList)

    def test_get_single_resource(self):
        response = CustomRequest.get('/unknown/2')
        Assertions.assert_code_status(response, 200)
        Assertions.validate_response_body(response, ResourceSingle)

    def test_get_single_resource_not_found(self):
        response = CustomRequest.get('/unknown/24')
        Assertions.assert_code_status(response, 404)
