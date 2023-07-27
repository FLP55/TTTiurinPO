from test_framework.steps_api import ApiSteps

def test_api_1_try_get_answer_without_data():
    ApiSteps().check_status_code_403(sol=None, camera=None, api_key=None, page=None, earth_date=None)