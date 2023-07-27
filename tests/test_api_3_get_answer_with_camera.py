import pytest

from test_data.data_for_tests import camera
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", camera)
def test_api_3_get_answer_with_camera(data):
    ApiSteps().check_status_code_403(sol=None, camera=data, api_key=None, page=None, earth_date=None)