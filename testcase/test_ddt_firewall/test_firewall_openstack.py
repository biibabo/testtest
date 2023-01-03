# -*- coding: utf-8 -*-

import unittest

from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestDisk(BaseCase):

    @file_data("../../testdata/test_firewall/test_firewall_openstack.json")
    def test_createdisk(self, Name, Rules, expect_code):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateFirewall"
        data = {
            "AccountId": 49,
            "OrgId": 1,
            "RegionEn": "RegionOne",
            "Name": Name,
            "Rules": Rules,
            "Platform": "openstack"
        }
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(expect_code, r.json()['RetCode'])


if __name__ == '__main__':
    unittest.main()
