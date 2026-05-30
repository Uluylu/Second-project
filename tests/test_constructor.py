from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_constructor_switch_to_buns_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Соус Spicy-X']")))

    driver.find_element(By.XPATH, "//span[text()='Булки']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")))

    driver.quit()

def test_constructor_switch_to_sauces_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Соус Spicy-X']")))
    
    driver.quit()

def test_constructor_switch_to_fillings_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")))
    
    driver.quit()