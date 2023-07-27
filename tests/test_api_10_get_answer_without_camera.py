import pytest

from test_data.data_for_tests import sol_and_page
from test_framework.steps_api import ApiSteps


@pytest.mark.parametrize('sol_data, page_data', sol_and_page)
def test_api_10_get_answer_without_camera(sol_data, page_data):
    ApiSteps().check_status_code_200(sol=sol_data, camera=None, api_key="DEMO_KEY", page=page_data, earth_date=None)