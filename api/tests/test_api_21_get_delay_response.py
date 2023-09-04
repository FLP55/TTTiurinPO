import pytest

from api.data_for_api_test.data_for_tests import random_number
from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
@pytest.mark.parametrize("data", random_number)
def test_api_21_get_delay_response(data):
    ApiSteps().get_delay_response(number_page=data)