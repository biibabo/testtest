#!/usr/bin/python
# -*- coding: UTF-8 -*-
from core.basecase import BaseCase


class TestRecycle(BaseCase):
    def test_recycle_on(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=UpdateRecycleBinConfig"
        data = {"State":1,"RemainingDay":2}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/setting/global',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual("成功", r.json()['Message'])
        # assert r.json()['RetCode'] == expect_code

    def test_recycle_off(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=UpdateRecycleBinConfig"
        data = {"State":2,"RemainingDay":2}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/setting/global',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(0, r.json()['RetCode'])
        self.assertEqual("成功", r.json()['Message'])
        # assert r.json()['RetCode'] == expect_code

    def test_recycle_vm(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetRecycleBinResources"
        data = {"ResourceType": "vm"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/recyclebin',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])

    def test_recycle_eip(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetRecycleBinResources"
        data = {"ResourceType": "eip"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/recyclebin',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])

    def test_recycle_disk(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetRecycleBinResources"
        data = {"ResourceType": "disk"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/recyclebin',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(0, r.json()['RetCode'])
