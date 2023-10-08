import subprocess
import logging

logger = logging.getLogger('google_dyndns.network_tools')

def get_host_ip(host):
  logger.debug(f'Looking up ip address of {host}')
  nslookup = subprocess.run(["nslookup", host], capture_output=True, encoding="utf-8")

  if nslookup.returncode == 0:
    address = nslookup.stdout[nslookup.stdout.find('Address: ')+9:nslookup.stdout.find('Address: ')+48].rstrip('\n')
    logger.debug(f'Ip address of {host} was resolved as {address}')
  else:
    address = null
    logger.debug(f'Ip address of {host} could not be resolved')
  return address

