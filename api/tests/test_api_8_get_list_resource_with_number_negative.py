import pytest

from api.data_for_api_test.data_for_tests import random_letter
from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
@pytest.mark.parametrize("data", random_letter)
def test_api_8_get_list_resource_with_number_negative(data):
    ApiSteps().get_list_resource_positive_with_number_negative(res_number=data)