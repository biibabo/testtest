# -*- coding: UTF-8 -*-
import time
import requests
from ddt import ddt, file_data
import unittest
from BeautifulReport import BeautifulReport
from core.basecase import BaseCase
import uuid
import json


# @ddt
class TestRSet(BaseCase):
    # @file_data("../../testdata/test_vm/test_vm_ucloud.json")
    # 创建ucloud云主机

    def test_01_CreateRSet(self):
        RSetName = uuid.uuid4()
        RSetName = str(RSetName)
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateRSet"
        data = {"RSetName": RSetName, "Description": "测试创建一个空资源集"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/resourceset/create',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual("成功", r.json()['Message'])
        self.assertEqual(0, r.json()['RetCode'])
        print(r.json()['Message'], "创建一个空资源集")
        bodystr = str(r.request.body, 'utf-8')
        bodyjson = json.loads(bodystr)
        RSetName = bodyjson['RSetName']
        globals()['RSetName'] = RSetName
        print('资源集名称为：', globals()['RSetName'])

    def test_02_GetRSetList(self):
        RSetName = globals()['RSetName']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetRSetList"
        data = {"Limit": 10, "Offset": 0, "Keyword": RSetName, "Status": [0], "FuzzyField": {}}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/resourceset',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        RSetId = r.json()['Data'][0]['RSetId']
        globals()['RSetId'] = RSetId
        print('资源集id为：', globals()['RSetId'])
        time.sleep(5)

    def test_03_DeleteRSet(self):
        RSetId = globals()['RSetId']
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=DeleteRSet"
        data = {"RSetId": RSetId}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/resourceset',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        print('删除', r.json()['Message'])
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual('成功', r.json()['Message'])


if __name__ == '__main__':
    # 创建类加载的对象
    load = unittest.TestLoader()
    # 将测试类加载到测试套件中
    suit1 = load.loadTestsFromTestCase(TestRSet)
    # 指定执行类中的一个方法或者整个类
    # suits = unittest.TestSuite([TestCreatevm("test_06_GetResourceDetail")])
    suits = unittest.TestSuite([suit1])
    report = BeautifulReport(suits)
    report.report(filename='TestRSet.html', description='TestRSet_测试报告', log_path='.',
                  report_dir='.',
                  theme='theme_memories')
