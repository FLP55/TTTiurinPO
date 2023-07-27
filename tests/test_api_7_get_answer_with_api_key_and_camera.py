import pytest

from test_data.data_for_tests import camera
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", camera)
def test_api_7_get_answer_with_api_key_and_camera(data):
    ApiSteps().check_status_code_200(sol=None, camera=data, api_key="DEMO_KEY", page=None, earth_date=None)