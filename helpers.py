import random


def generate_random_user():
    names_list = ["Иван", "Алексей", "Мария", "Дмитрий", "Елена", "Сергей", "Ольга"]
    email_list = ["gmail.com", "yandex.ru", "ya.ru", "mail.ru", "inbox.ru"]
    random_name = f"{random.choice(names_list)}{random.randint(100,999)}"
    random_login = f"Valery_Plotarev_45_{random.randint(100,999)}@{random.choice(email_list)}"
    random_valid_password = f"{random.randint(100000,999999)}"
    random_invalid_password = f"{random.randint(100,99999)}"

    return {
        "name": random_name,
        "email": random_login,
        "valid_password": random_valid_password,
        "invalid_password": random_invalid_password
    }
