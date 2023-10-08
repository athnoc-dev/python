import os, logging, browser
from dotenv import load_dotenv
from ip_updater import update_dynamic_ip_google_domains
from network_tools import get_host_ip

def setup_env_vars():
  global user
  global password
  global fqdn
  try:
    load_dotenv()
    user = os.getenv('google_dyndns_user')
    password = os.getenv('google_dyndns_password')
    fqdn = os.getenv('google_dyndns_fqdn')
    logger.debug('Secrets loaded')
  except:
    logger.info('Application halted because loading secrets failed')
    quit() 
  
def setup_logging():
  global logger
  logger = logging.getLogger('google_dyndns')
  logger.setLevel(logging.DEBUG)
  c_handler = logging.StreamHandler()
  f_handler = logging.FileHandler('google_dyndns.log')
  f_handler.setLevel(logging.INFO)
  c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
  f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  c_handler.setFormatter(c_format)
  f_handler.setFormatter(f_format)
  logger.addHandler(c_handler)
  logger.addHandler(f_handler)

def get_router_ip():
  browser.driver.get('http://192.168.1.1/')
  browser.driver.set_window_size(1080, 1024)
  browser.element_click('Frm_Username')
  browser.element_send_keys('Frm_Username', 'user')
  browser.element_click('Frm_Password')
  browser.element_send_keys('Frm_Password', 'user')
  browser.element_click('LoginId')
  browser.element_click('internet')
  browser.element_click('EthStateDevBar')
  ip_str = browser.element_wait('cIPAddress:0').text
  browser.element_click('LogOffLnk')
  ip = ip_str.split('/')[0]
  return ip

def main():
  setup_logging()
  setup_env_vars()
  browser.setup_webdriver()

  try:
    router_ip = get_router_ip()
  except Exception as e:
    browser.teardown_webdriver()
    logger.debug("The application failed and reported the following: ", e)
    quit()

  browser.teardown_webdriver()
  host_ip = get_host_ip(fqdn)

  if host_ip != router_ip:
    logger.info(f'Host {fqdn} ip address [{host_ip}] is not the same as router WAN ip address [{router_ip}]')
    update_dynamic_ip_google_domains(user, password, fqdn, router_ip)
  else:
    logger.info(f'Host {fqdn} ip address [{host_ip}] is the same as router WAN ip address [{router_ip}]. No need for an update.')

# main
main()
