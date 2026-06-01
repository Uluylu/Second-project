from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
import locators


def test_login_through_main_page_button_success(driver, create_valid_user):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.MAIN_AUTH_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.AUTH_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    driver.find_element(*locators.AUTH_PASSWORD_INPUT).send_keys(create_valid_user["password"])
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(locators.MAIN_ORDER_BUTTON))

    assert driver.current_url == constants.BASE_URL

def test_login_through_personal_account_success(driver, create_valid_user):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.HEADER_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.AUTH_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    driver.find_element(*locators.AUTH_PASSWORD_INPUT).send_keys(create_valid_user["password"])
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(locators.MAIN_ORDER_BUTTON))

    assert driver.current_url == constants.BASE_URL

def test_login_through_registration_form_success(driver, create_valid_user):
    driver.get(constants.REGISTER_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.REG_LOGIN_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.AUTH_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    driver.find_element(*locators.AUTH_PASSWORD_INPUT).send_keys(create_valid_user["password"])
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(locators.MAIN_ORDER_BUTTON))

    assert driver.current_url == constants.BASE_URL

def test_login_through_forgot_password_form_success(driver, create_valid_user):
    driver.get(constants.FORGOT_PASSWORD_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PASS_AUTH_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.AUTH_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    driver.find_element(*locators.AUTH_PASSWORD_INPUT).send_keys(create_valid_user["password"])
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(locators.MAIN_ORDER_BUTTON))

    assert driver.current_url == constants.BASE_URL
