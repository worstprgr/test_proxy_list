#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import time
import os

proxy_white = 'proxy_white.txt'
proxy_list = 'proxy_list.csv'
test_target = 'https://ipinfo.io/json'

# del txt
try:
    txt_empty = os.stat(proxy_white).st_size != 0
    if txt_empty is True:
        os.remove(proxy_white)
except FileNotFoundError:
    pass

line_counter = sum(1 for line in open(proxy_list))
# line_counter = 3

print('[PROXY TEST]: ' + str(line_counter) + ' proxy servers in queue ...')

with open(proxy_list, 'r', encoding='utf8') as f:
    for x in range(line_counter):
        try:
            adress = f.readline().replace(', ', ':')[:-1]
            print('[' + str(x) + '/' + str(line_counter) + '] ' + '[Checking]: ' + adress)
            response = requests.get(test_target, proxies={'https': adress})
            print(response.json()['ip'] + ' - ' + response.json()['country'])
            print('[SUCCESS!]')
            with open(proxy_white, 'a+', encoding='utf8') as d:
                d.write(adress + '\n')
        except:
            print('Connection Timeout of IP: ' + adress)
            time.sleep(1)
            pass


# response = requests.get("https://ipinfo.io/json")

