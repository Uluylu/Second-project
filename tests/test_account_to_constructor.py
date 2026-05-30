from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_personal_account_go_to_constructor_on_button_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']")))

    driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()
 
    
def test_personal_account_go_to_constructor_on_logo_success(create_valid_user):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    user_login = create_valid_user["email"]
    user_password = create_valid_user["password"]

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[label[text()='Email']]/input"))).send_keys(user_login)
    driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']")))

    driver.find_element(By.XPATH, "//a[@href='/']").click()
    
    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    driver.quit()
