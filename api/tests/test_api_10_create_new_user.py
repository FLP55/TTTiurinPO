import pytest

from api.data_for_api_test.data_for_tests import data_for_create_user
from api.test_framework.steps_api import ApiSteps


@pytest.mark.parametrize('name, job', data_for_create_user)
def test_api_10_create_new_user(name, job):
    ApiSteps().create_new_user(name=name, job=job)