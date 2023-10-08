import logging
import requests

logger = logging.getLogger('google_dyndns.ip_updater')

def update_dynamic_ip_google_domains(user, password, fqdn, ip):
  logger.debug(f'Updating Google Domains host [{fqdn}] with ip address [{ip}]')
  try:
    response = requests.post('https://domains.google.com/nic/update?hostname=' + fqdn + '&myip=' + ip, auth=(user, password))
  except Exception as e:
    logger.error('POST request to Google Domains url raised an exception: ', e)

  if response.status_code == 200:
    logger.debug(f'Google Domains API responds: status code {response.status_code} -- {response.text} --')
    logger.info(f'Host [{fqdn}] successfully updated with ip address [{ip}]')
  else:
    logger.error(f'Google Domains API returns an error: status code {response.status_code} -- {response.text} --')
