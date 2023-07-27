import pytest

from test_data.data_for_tests import page
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", page)
def test_api_8_get_answer_with_api_key_and_page(data):
    ApiSteps().check_status_code_200(sol=None, camera=None, api_key="DEMO_KEY", page=data, earth_date=None)