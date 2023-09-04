import pytest

from api.data_for_api_test.data_for_tests import data_for_update_user_data_negative
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize('name, job, user_number', data_for_update_user_data_negative)
def test_api_13_update_user_negative(name, job, user_number):
    ApiSteps().update_user_with_put_negative(user_number=user_number, name=name, job=job)