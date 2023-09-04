from typing import Any


class DataPayload:

    @staticmethod
    def get_payload_for_create_new_user(name: str, job: str) -> Any:
        return {
            "name": name,
            "job": job
        }

    @staticmethod
    def get_payload_for_register_user(email: str, password: str) -> Any:
        return {
            "email": email,
            "password": password
        }

    @staticmethod
    def get_payload_for_register_user_negative(email: str) -> Any:
        return {
            "email": email
        }