import pytest

from api.data_for_api_test.data_for_tests import data_for_create_user_negative
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize('name, job', data_for_create_user_negative)
def test_api_11_create_new_user_negative(name, job):
    ApiSteps().create_new_user_negative(name=name, job=job)