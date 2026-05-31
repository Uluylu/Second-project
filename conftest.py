import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
import helpers
import locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def create_valid_user(driver):
    user = helpers.generate_random_user()
    driver.get(constants.REGISTER_URL)

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REG_NAME_INPUT)).send_keys(user["name"])
    driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(user["valid_password"])
    driver.find_element(*locators.REG_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(locators.LOGIN_SUBMIT_BUTTON))

    return {"email": user["email"], "password": user["valid_password"]}
