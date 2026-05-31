from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
import locators


def test_personal_account_logout_success(driver, create_valid_user):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.HEADER_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.AUTH_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    driver.find_element(*locators.AUTH_PASSWORD_INPUT).send_keys(create_valid_user["password"])
    driver.find_element(*locators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(locators.HEADER_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PROFILE_LOGOUT_BUTTON)).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_SUBMIT_BUTTON))

    assert driver.current_url == constants.AUTHORIZATION_URL
