from test_framework.steps_api import ApiSteps

def test_api_13_get_answer_with_earth_date_and_api_key():
    ApiSteps().check_status_code_200(sol=None, camera=None, api_key="DEMO_KEY", page=None, earth_date="2012-12-03")