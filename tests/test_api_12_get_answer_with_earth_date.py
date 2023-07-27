from test_framework.steps_api import ApiSteps

def test_api_12_get_answer_with_earth_date():
    ApiSteps().check_status_code_403(sol=None, camera=None, api_key=None, page=None, earth_date="2012-12-03")