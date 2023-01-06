# -*- coding: UTF-8 -*-
import time
from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestEip(BaseCase):
    global resourceid

    @file_data("../../testdata/test_eip/test_eip_ucloud.json")
    def test_01_createucloudeip(self, EIPInstance, expect_code):
        global resourceid
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateEIP"
        data = {"OrgId": 1,
                "AccountId": 2,
                "Platform": "ucloud",
                "EIPInstance": EIPInstance
                }
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(expect_code, r.json()['RetCode'])
        resourceid = r.json()["Data"]["ResourceId"]
        print(resourceid, 'resourceid=====')

    def test_02_eip_status(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail"
        data = {"cmpUuid": resourceid, "ResourceType": "eip"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        startTime = time.time()
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()["Data"] == {} or r.json()["Data"]["Status"] != 1:
                continue
            elif r.json()["Data"]["Status"] == 1:
                break
            else:
                print('查询异常')
            time.sleep(2)
            endTime = time.time()
            if endTime - startTime > 60:
                raise Exception("在60s内查询结果失败")

        Status = r.json()["Data"]["Status"]
        self.assertEqual(1, Status)
        print(r.json())

    def test_03_modifyucloudeip(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=ModifyBandWidthEIP"
        data = {"EIPInstances":
                    [{"Bandwidth": 2,
                      "AccountId": 2,
                      "Platform": "ucloud",
                      "ProjectId": "org-uzao3s",
                      "Region": "cn-sh2",
                      "ResourceId": resourceid}]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])

    def test_04_eipbandwidth(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail"
        data = {"cmpUuid": resourceid, "ResourceType": "eip"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        startTime = time.time()
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()["Data"]["Bandwidth"] == 1:
                continue
            elif r.json()["Data"]["Bandwidth"] == 2:
                break
            else:
                print('查询异常')
            time.sleep(2)
            endTime = time.time()
            if endTime - startTime > 60:
                raise Exception("在60s内查询结果失败")

    def test_05_delucloudeip(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=DeleteEIP"
        data = {"ResourceIds": [resourceid]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/eip',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        print(r.json())
