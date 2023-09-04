from test_data.random_data import get_random_digits, get_random_string, get_double_random_digits, \
    get_random_string_for_payload, get_random_email

#случайное число
random_number = [get_random_digits(), get_random_digits(), get_random_digits()]

#случайная буква
random_letter = [get_random_string(), get_random_string(), get_random_string()]

#Двухзначное число
random_double_number = [get_double_random_digits(), get_double_random_digits(), get_double_random_digits()]

#Данные для создания пользователя
data_for_create_user = [
    (get_random_string_for_payload(), get_random_string_for_payload()),
    (get_random_string_for_payload(), get_random_string_for_payload()),
    (get_random_string_for_payload(), get_random_string_for_payload())
]
data_for_create_user_negative = [
    (get_random_digits(), get_random_digits()),
    (get_random_digits(), get_random_digits()),
    (get_random_digits(), get_random_digits())
]

#data для изменения данных пользователя
data_for_update_user_data = [
    (get_random_string_for_payload(), get_random_string_for_payload(), get_random_digits()),
    (get_random_string_for_payload(), get_random_string_for_payload(), get_random_digits()),
    (get_random_string_for_payload(), get_random_string_for_payload(), get_random_digits())
]
data_for_update_user_data_negative = [
    (get_random_digits(), get_random_digits(), get_random_digits()),
    (get_random_digits(), get_random_digits(), get_random_digits()),
    (get_random_digits(), get_random_digits(), get_random_digits())
]

#data для регистрации пользователя
data_for_register_user = [
    (get_random_email(),get_random_string(password_len=8)),
    (get_random_email(),get_random_string()),
    (get_random_email(),get_random_string())
]

data_for_register_user_unsuccessful = [get_random_email(), get_random_email(), get_random_email()]