import json


class Assertions:

    @staticmethod
    def assert_code_status(response, expected_status_code):
        assert response.status_code == expected_status_code, f"Wrong status code to url {response.url}"

    @staticmethod
    def validate_response_body(response, schema):
        schema.parse_obj(response.json())

    @staticmethod
    def assert_response_values(response, data, values):
        for item in values:
            assert response.json().get(item) == data.get(item), f"Wrong response data {item}"

    @staticmethod
    def assert_response_body(response, expected_response_body):
        if response.text != '' and expected_response_body != '':
            response_json = response.json()
            expected_response_body_json = json.loads(expected_response_body)
            if "id" in response_json and "id" in expected_response_body:
                response_json["id"] = None
                expected_response_body_json["id"] = None
            if "createdAt" in response_json and "createdAt" in expected_response_body:
                response_json["createdAt"] = None
                expected_response_body_json["createdAt"] = None
            if "updatedAt" in response_json and "updatedAt" in expected_response_body:
                response_json["updatedAt"] = None
                expected_response_body_json["updatedAt"] = None
            print(response_json)
            print(expected_response_body_json)
            assert response_json == expected_response_body_json

