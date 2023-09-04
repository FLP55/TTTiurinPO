import pytest

from api.data_for_api_test.data_for_tests import random_number
from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
@pytest.mark.parametrize("data", random_number)
def test_api_7_get_list_resource_positive_with_number(data):
    ApiSteps().get_list_resource_positive_with_number_positive(res_number=data)