import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def create_valid_user():
    names_list = ["Иван", "Алексей", "Мария", "Дмитрий", "Елена", "Сергей", "Ольга"]
    random_name = f"{random.choice(names_list)}{random.randint(100,999)}"
    random_login = f"Valery_Plotarev_45_{random.randint(100,999)}@yandex.ru"
    random_password = f"{random.randint(100000,999999)}"

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[label[text()='Имя']]/input"))).send_keys(random_name)
    driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(random_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(random_password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.quit()

    return {"email": random_login, "password": random_password}