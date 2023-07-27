import pytest

from test_data.data_for_tests import sol_and_cam
from test_framework.steps_api import ApiSteps


@pytest.mark.parametrize('sol_data, camera_data', sol_and_cam)
def test_api_9_get_answer_without_page(sol_data, camera_data):
    ApiSteps().check_status_code_200(sol=sol_data, camera=camera_data, api_key="DEMO_KEY", page=None, earth_date=None)
