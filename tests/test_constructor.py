from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time
import constants
import locators


def test_constructor_switch_to_buns_success(driver):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.TAB_SAUCES)).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.TAB_BUNS)).click()
    time.sleep(1)

    class_buns = driver.find_element(*locators.TAB_BUNS).get_attribute("class")

    assert "tab_tab_type_current__2BEPc" in class_buns

def test_constructor_switch_to_sauces_success(driver):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.TAB_SAUCES)).click()
    time.sleep(1)

    class_sauces = driver.find_element(*locators.TAB_SAUCES).get_attribute("class")

    assert "tab_tab_type_current__2BEPc" in class_sauces

def test_constructor_switch_to_fillings_success(driver):
    driver.get(constants.BASE_URL)

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.TAB_FILLINGS)).click()
    time.sleep(1)

    class_fillings = driver.find_element(*locators.TAB_FILLINGS).get_attribute("class")

    assert "tab_tab_type_current__2BEPc" in class_fillings
