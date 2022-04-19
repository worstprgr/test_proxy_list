#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import csv
import time

# config
chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--no-sandbox")
# s=Service('/usr/bin/chromedriver') #Linux
s = Service('C:/chromedriver/chromedriver.exe')  # Windows

driver = webdriver.Chrome(service=s, options=chromeOptions)


# user interaction
cond_proxy = input('Do you want to update/create the proxy list? Type y or n: ')

# Get proxy list
# if 0 == 1:  # debug
if cond_proxy == 'y':
    # target
    proxy_url = 'https://free-proxy-list.net/'

    # lists
    ip = []
    port = []

    p_file = 'proxy_raw.txt'
    proxy_list = 'proxy_list.csv'

    # scrape proxy list
    driver.get(proxy_url)
    time.sleep(1)

    # get table size
    table = driver.find_element(By.XPATH, '//table/tbody[1]').get_attribute('innerText')

    with open(p_file, 'w+', encoding='utf8') as f:
        f.writelines(table)

    line_counter = sum(1 for line in open(p_file))

    print('[1/3]: Table contains ' + str(line_counter) + ' items.')

    # get IP and PORT
    print("[2/3]: Collecting IPs and ports ...")

    for x in range(1, line_counter+1):
        ip.append(str(driver.find_element(
            By.XPATH, '//table/tbody/tr[' + str(x) + ']/td[1]').get_attribute('innerText')))

    for x in range(1, line_counter+1):
        port.append(str(driver.find_element(
            By.XPATH, '//table/tbody/tr[' + str(x) + ']/td[2]').get_attribute('innerText')))

    driver.quit()

    # save clean proxy list
    with open(proxy_list, 'w+', encoding='utf8') as f:
        for x in range(line_counter):
            f.write(ip[x] + ', ' + port[x] + '\n')

    print("[3/3]: Saved IPs and Ports!")
else:
    print('Skipping the update.')

