import pytest

from api.data_for_api_test.data_for_tests import data_for_update_user_data
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize('name, job, user_number', data_for_update_user_data)
def test_api_15_update_user_with_patch_negative(name, job, user_number):
    ApiSteps().update_user_with_patch_negative(user_number=user_number, name=name, job=job)