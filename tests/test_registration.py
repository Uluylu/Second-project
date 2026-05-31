from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
import locators
import helpers


def test_registration_success(driver):
    user = helpers.generate_random_user()
    driver.get(constants.BASE_URL)
    
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.HEADER_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.REG_REGISTER_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REG_NAME_INPUT)).send_keys(user["name"])
    driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(user["valid_password"])
    driver.find_element(*locators.REG_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(locators.LOGIN_SUBMIT_BUTTON))
    
    assert driver.current_url == constants.AUTHORIZATION_URL

def test_registration_incorrect_password_error(driver):
    user = helpers.generate_random_user()
    driver.get(constants.REGISTER_URL)
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REG_NAME_INPUT)).send_keys(user["name"])
    driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(user["invalid_password"])
    driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(user["email"])

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(locators.REG_PASSWORD_ERROR))

    assert driver.current_url == constants.REGISTER_URL
