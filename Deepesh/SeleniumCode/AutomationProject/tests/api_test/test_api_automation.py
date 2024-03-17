import pytest
from base.api_base_code import APIBase
from data.session_data import *
from data.api_data import *

class TestAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj = APIBase(api_url=api_url)

    def test_get_object_details_and_verify(self):
        response = self.api_obj.get_method(object_id_get_details)
        assert response[1] == 200

    def test_create_new_object_and_verify(self):
        response = self.api_obj.post_method(headers=headers, payload=create_obj_payload)
        assert response[1] == 200
        print(response[0])
