import pytest

from api.data_for_api_test.data_for_tests import random_double_number
from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
@pytest.mark.parametrize("data", random_double_number)
def test_api_9_get_list_resource_with_double_number(data):
    ApiSteps().get_list_resource_positive_with_number_negative(res_number=data)
