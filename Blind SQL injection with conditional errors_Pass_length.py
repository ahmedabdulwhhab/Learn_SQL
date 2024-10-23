# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def send_http_request(url):
    import requests     #pip install requests

    url = "https://0a3100e00345b5608318aad800f500a4.web-security-academy.net/"

    response = requests.get(url)

    print(response.status_code)
    print(response.headers)
    ###################################################
    response = requests.request("get", url=url, headers=response.headers);

    print("line 12")
    print(response.status_code)
    print(response.headers)

    ###################################################
    response = requests.request("get", url=url, headers=response.headers);

    print("Line 19")
    print(response.status_code)
    print(response.headers)

    ###################################################
    response = requests.request("get", url=url, headers=response.headers);
    print("Line 25")
    print(response.status_code)
    print(response.headers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    url = "https://0a3100e00345b5608318aad800f500a4.web-security-academy.net/"
    send_http_request(url)
    url = "https://0a3100e00345b5608318aad800f500a4.web-security-academy.net/filter?category=Pets"
    send_http_request(url)
    url = "https://0a3100e00345b5608318aad800f500a4.web-security-academy.net/filter?category=Pets"
    send_http_request(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
