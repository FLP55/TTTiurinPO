from api.data_for_api_test.api_data import DataPayload
from api.test_framework.main_checkers import CommonChecker
from api.test_framework.requests import RequestForTestApi


class ApiSteps:

    def __init__(self) -> None:
        self.request = RequestForTestApi()
        self.data = DataPayload()

    def get_user_list_positive(self, number_page: int):
        response = self.request.get_list_user(number_page)
        CommonChecker.check_status_code_200(response, assertion_message="Запрос отправлен некорректно")

    def get_user_list_negative(self, number_page: str):
        response = self.request.get_list_user(number_page)
        CommonChecker.check_status_code_404(response, assertion_message="Запрос отправлен корректно")

    def get_single_user_positive(self, user_number: int):
        response = self.request.get_list_user(user_number)
        CommonChecker.check_status_code_200(response, assertion_message="Запрос отправлен некорректно")

    def get_single_user_negative(self, user_number: any):
        response = self.request.get_list_user(user_number)
        CommonChecker.check_status_code_404(response, assertion_message="Запрос отправлен корректно")

    def get_list_resource_positive(self,):
        response = self.request.get_list_resource()
        CommonChecker.check_status_code_200(response, assertion_message="Запрос отправлен некорректно")

    def get_list_resource_positive_with_number_positive(self, res_number: any):
        response = self.request.get_list_resource_with_number(res_number=res_number)
        CommonChecker.check_status_code_200(response, assertion_message="Запрос отправлен некорректно")

    def get_list_resource_positive_with_number_negative(self, res_number: any):
        response = self.request.get_list_resource_with_number(res_number=res_number)
        CommonChecker.check_status_code_404(response, assertion_message="Запрос отправлен корректно")

    def create_new_user(self, name: any, job: any):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.create_user(payload)
        CommonChecker.check_status_code_201(response, assertion_message="Не удалось создать пользователя")

    def create_new_user_negative(self, name: any, job: any):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.create_user(payload)
        CommonChecker.check_status_code_404(response, assertion_message="Удалось создать пользователя")

    def update_user_with_put(self, name, job, user_number):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.update_user(user_number=user_number, payload=payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось обновить пользователя")

    def update_user_with_put_negative(self, name, job, user_number):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.update_user(user_number=user_number, payload=payload)
        CommonChecker.check_status_code_404(response, assertion_message="Удалось обновить пользователя")

    def update_user_with_patch(self, name, job, user_number):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.update_user_patch(user_number=user_number, payload=payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось обновить пользователя")

    def update_user_with_patch_negative(self, name, job, user_number):
        payload = self.data.get_payload_for_create_new_user(name, job)
        response = self.request.update_user_patch(user_number=user_number, payload=payload)
        CommonChecker.check_status_code_404(response, assertion_message="Удалось обновить пользователя")

    def delete_user(self, number_page: int):
        response = self.request.delete_user(number_page)
        CommonChecker.check_status_code_204(response, assertion_message="Запрос отправлен некорретно")

    def register_new_user(self, email: str, password: str):
        payload = self.data.get_payload_for_register_user(email=email, password=password)
        response = self.request.register_user(payload=payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось зарегистрировать пользователя")

    def register_new_user_negative(self, email: str):
        payload = self.data.get_payload_for_register_user_negative(email=email)
        response = self.request.register_user(payload=payload)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось зарегистрировать пользователя")

    def login_hard_user(self, email: str, password: str):
        payload = self.data.get_payload_for_register_user(email=email, password=password)
        response = self.request.login_user(payload=payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось авторизовать пользователя")

    def login_hard_user_negative(self, email: str):
        payload = self.data.get_payload_for_register_user_negative(email=email)
        response = self.request.login_user(payload=payload)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось зарегистрировать пользователя")

    def get_delay_response(self, number_page: int):
        response = self.request.get_list_user(number_page)
        CommonChecker.check_status_code_200(response, assertion_message="Запрос отправлен некорректно")
