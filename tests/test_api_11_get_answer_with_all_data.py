import pytest

from test_data.data_for_tests import all_data
from test_framework.steps_api import ApiSteps


@pytest.mark.parametrize('sol_data, camera_data, page_data', all_data)
def test_api_11_get_answer_with_all_data(sol_data, camera_data, page_data):
    ApiSteps().check_status_code_200(
        sol=sol_data, camera=camera_data, api_key="DEMO_KEY", page=page_data, earth_date=None
    )