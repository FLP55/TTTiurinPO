import pytest

from test_data.data_for_tests import sol
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", sol)
def test_api_6_get_answer_with_api_key_and_sol(data):
    ApiSteps().check_status_code_200(sol=data, camera=None, api_key="DEMO_KEY", page=None, earth_date=None)