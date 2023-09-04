import pytest

from api.data_for_api_test.data_for_tests import data_for_update_user_data
from api.test_framework.steps_api import ApiSteps


@pytest.mark.parametrize('name, job, user_number', data_for_update_user_data)
def test_api_12_update_user(name, job, user_number):
    ApiSteps().update_user_with_put(user_number=user_number, name=name, job=job)