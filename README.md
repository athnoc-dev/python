# Google Dynamic DNS updater
## Description
I am one of those who are unfortunate enough to be behind a Carrier Grade NAT (a NAT implemented by an ISP).<br><br> 
This means that the ISP uses NAT before letting you go on the Internet. What happens is the following:<br> 
**My network -> Router (NAT 1) -> ISP router (NAT 2) -> Internet**<br><br> 
The ISP router ip address will block any port forwards to my internal network.<br><br>
However, I found that the NAT 1 address was actually a reservered WAN ip address range and is accessible from the Internet directly.<br> 
When trying to update my ip address directly with through the Google Domains Dynamic DNS API, it reads the NAT 2 ip address sent by the browser.<br><br>
So the easy way does not work.<br><br> 
This small script logs into the router and retrieve the WAN ip address and updates the ip address through the Google Domains Dynamic DNS API automatically.<br><br> 
For the browser automation I have used Selenium with a headless Firefox webdriver.<br><br> 
The POST method for the API is done with the Python requests library.

## Requirements
Selenium<br> 
How to install Selenium, a browser and a webdriver<br><br> 

Requests

## Usage
Run google_dyndns.py <br> 
Debug logging to console and info to google_dyndns.log<br> 
