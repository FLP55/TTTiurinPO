import pytest

from test_data.data_for_tests import page
from test_framework.steps_api import ApiSteps

@pytest.mark.parametrize("data", page)
def test_api_4_get_answer_with_page(data):
    ApiSteps().check_status_code_403(sol=None, camera=None, api_key=None, page=data, earth_date=None)