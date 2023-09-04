import pytest

from api.test_framework.steps_api import ApiSteps
@pytest.mark.api
def test_api_6_get_list_resource_positive():
    ApiSteps().get_list_resource_positive()