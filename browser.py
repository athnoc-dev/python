from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

logger = logging.getLogger('google_dyndns.browser')

def setup_webdriver():
  global driver
  options = webdriver.FirefoxOptions()
  options.add_argument("-headless")
  driver = webdriver.Firefox(options=options)
  logger.debug("Web driver initialized")

def teardown_webdriver():
  driver.quit()
  logger.debug("Web driver exited")

def convert_to_xpath(element_id):
  xpath_element = '//*[@id="' + element_id + '"]'
  return xpath_element

def element_wait(element_id):
  xpath_element = convert_to_xpath(element_id)
  element = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_element)))
  logger.debug(f'Element [{element_id}] is available')
  return element

def element_click(element_id):
  xpath_element = convert_to_xpath(element_id)
  driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_element))))
  logger.debug(f'Clicked on element [{element_id}]')

def element_send_keys(element_id, input):
  element_wait(element_id).send_keys(input)
  logger.debug(f'Send input to element [{element_id}]')  
