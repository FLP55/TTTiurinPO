import pytest

from api.data_for_api_test.data_for_tests import random_letter
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize("data", random_letter)
def test_api_2_get_list_user_with_invalid_data(data):
    ApiSteps().get_user_list_negative(number_page=data)