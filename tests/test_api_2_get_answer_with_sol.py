import pytest

from test_data.data_for_tests import sol
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", sol)
def test_api_2_get_answer_with_sol(data):
    ApiSteps().check_status_code_403(sol=data, camera=None, api_key=None, page=None, earth_date=None)