import os
import requests

def send_plus_msg(msg):
    global token
    url = f"http://www.pushplus.plus/send?token={token}&title={msg}&content={msg}&template=html"
    print(url)
    requests.get(url)


def get_cookies(user, passwd):
    url = 'https://www.wanbianios.com/wp-admin/admin-ajax.php'
    headers = {
        "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
    }
    data = {
        'action':'user_login',
        'username':user,
        'password':passwd
    }
    response = requests.post(url=url, data=data, headers=headers)
    response.encoding = 'utf-8'
    return response.cookies

token = os.environ.get('TOKEN')
user = os.environ.get('USER')
passwd = os.environ.get('PASSWD')
print(token)
print(user)
print(passwd)


headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
}

response = requests.post("https://www.wanbianios.com/wp-admin/admin-ajax.php", data="action=user_qiandao", headers=headers, cookies=get_cookies(user=user, passwd=passwd))
response.encoding = 'utf-8'
print("status_code:", response.status_code)
print("response:", response.json())

if response.text == "0":
    print("错误，请检查COOKIES")
    # send_plus_msg("签到错误，请检查COOKIES，返回值：" + response.text)
elif response.json()['status'] == "1":
    print(response.json()['msg'])
    # send_plus_msg(response.json()['msg'])
elif response.json()['status'] == "0":
    msg = response.json()['msg']
    print(msg)
    # if msg == '请登录后签到':
        # send_plus_msg("Cookie过期：请前往Github-项目页面-Setting-Secret更新Cookie")
else:
    print("未知错误")
    # send_plus_msg("未知错误：" + response.text)
