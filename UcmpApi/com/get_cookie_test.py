import pytest
import requests

url = "https://cmp-fe.ucloud.cn/api/gateway?Action=Login"
data = {"AccountId": "admin", "Password": "039b091873fbc2f68abe7723b4ac018d"}



# 1.获取请求头中的cookie
def test_get_req_cookie(self):
        # 创建session对象，使用session发送post请求来获取cookie的值
        session = requests.Session()
        session.post(url, data=data)
        req_cookies = session.cookies.get_dict()
        print(req_cookies)  #可以打印出来看下有没有获取到
        return req_cookies

# 获取响应头中的cookie
def test_get_res_cookie(self):  # 获取cookie
        response_headers = requests.post(url,data=data).headers  # 获取响应头信息
        print("response_headers:", response_headers)  # 打印响应头部信息确认下响应头中是否有Cookie这个参数
        res_cookies = requests.post(url,data=data).headers["Set-Cookie"]  # 如果响应头中没有cookie这个参数，那么会报KeyError:cookie错误
        print("response_cookies:", res_cookies)  # 打印出来看下响应头中的cookie值是什么
        return res_cookies


# if __name__ == '__main__':
#     pytest.main(['get_cookie_test.py'])
