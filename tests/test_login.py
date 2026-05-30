from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_through_main_page_button_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    driver.quit()


def test_login_through_personal_account_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    driver.quit()

def test_login_through_registration_form_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    driver.quit()

def test_login_through_forgot_password_form_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/forgot-password")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

    driver.quit()
