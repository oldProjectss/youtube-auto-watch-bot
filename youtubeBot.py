from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
import random

# get the proxies from proxy.txt and store it into proxy_list array
# get a rendom proxy every time the while loop runs
#

proxy_list = []

with open('proxy.txt') as fil:
    proxy_list = [i.strip() for i in fil]

timeToReopenBrowser = 0
while timeToReopenBrowser <= 3:
    proxies = random.choice(proxy_list)
    proxy_ip_port = proxies

    print("The proxy used is:", proxy_ip_port)

    # set proxy

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    # let's call the browser

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.get("https://www.myip.com/")

    sleep(3)

    # close browser

    driver.quit()

    timeToReopenBrowser += 1

# https://openproxy.space/api replace static proxies
