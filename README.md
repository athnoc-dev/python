# Google Dynamic DNS updater
## Description
I am one of those who are unfortunate enough to be behind a [Carrier-grade NAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT) (a NAT implemented by an ISP).<br><br> 
This means that the ISP uses NAT **TWICE** before letting you go on the Internet. What happens is the following:<br><br>
**My network -> Router (NAT 1) -> ISP router (NAT 2) -> Internet**<br><br> 
The ISP router ip address will block any port forwards to my internal network coming via **NAT 2**.<br><br>
However, I found that the **NAT 1** address is actually a [Shared Address Space](https://rdap.arin.net/registry/ip/100.64.0.0) and is accessible from the Internet directly.<br> 
When trying to update my ip address directly through the [Google Domains Dynamic DNS API](https://support.google.com/domains/answer/6147083?hl=en#:~:text=Update%20your%20Dynamic%20DNS%20record%20with%20the%20API), it reads the **NAT 2** ip address [sent by the browser](https://support.google.com/domains/answer/6147083?hl=en#:~:text=If%20not%20supplied%2C%20we%20use%20the%20IP%20of%20the%20agent%20that%20sent%20the%20request.).<br><br>
So the easy way does not work.<br><br> 
This small script logs into the router and retrieve the WAN ip address (**NAT 1**) and updates the ip address through the Google Domains Dynamic DNS API automatically.<br><br> 
For the browser automation I have used Selenium with a headless Firefox webdriver.<br>
The POST method for the API is done with the Python requests library.

## Requirements
Selenium<br> 
How to install Selenium, a browser and a webdriver<br><br> 

Requests

## Usage
Run google_dyndns.py <br> 
Debug logging to console and info to google_dyndns.log<br> 
