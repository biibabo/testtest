import unittest
# 定义BaseCase去继承unittest.TestCase，说明它是一个测试类
import requests

from common import logger
from configcenter import configdata


class BaseCase(unittest.TestCase):
    # class方法
    @classmethod
    # unittest中的一个特殊的方法，所有的方法执行之前会先执行这个方法
    def setUpClass(cls) -> None:
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=Login"
        data = {"AccountId": configdata['config']['AccountId'], "Password": configdata['config']['Password']}
        r = cls.request(method="post", url=url, json=data)
        print(r.json())
        print(r.headers['Set-Cookie'])
        cls.cookie = r.headers['Set-Cookie']
        assert r.json()['RetCode'] == 0

    @classmethod
    def request(cls, method: str, url, params=None, data=None, json=None, **args):
        """
        自定义发送请求
        :param method: 请求方法
        :param url: 请求的URL
        :param params: 请求参数
        :param data: body data
        :param json: json格式
        :param args: 其他字典参数
        :return:
        """
        method = method.upper()
        if method == "GET":
            res = requests.get(url, params=params, **args)
            logger.info(f'请求方式: {method}，请求url: {url}, 请求参数：{res.request.body}, 服务器返回结果：{res.text}')
            return res
        elif method == "POST":
            res = requests.post(url, data=data, json=json, **args)
            logger.info(f'请求方式: {method}，请求url: {url}, 请求参数：{res.request.body}, 服务器返回结果：{res.text}')
            return res
