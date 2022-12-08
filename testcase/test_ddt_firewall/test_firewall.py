import unittest

from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestFirewall(BaseCase):
    @file_data("../../testdata/test_firewall/test_firewall_ucloud.json")
    def test_createucloudfirewall(self, name, Rules, expect_code):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateFirewall"
        data = {
            "AccountId": 2,
            "OrgId": 1,
            "RegionEn": 'cn-sh2',
            "Name": name,
            "Rules": Rules,
            "Platform": "ucloud"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(expect_code, r.json()['RetCode'])
        # assert r.json()['RetCode'] == expect_code

    @unittest.skip("null")
    # @file_data("../../testdata/firewall/testaliyunfirewall.json")
    def test_createfirewall(self, name, Rules, expect_code):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateFirewall"
        data = {
            "AccountId": 2,
            "OrgId": 1,
            "RegionEn": 'cn-sh2',
            "Name": name,
            "Rules": Rules,
            "Platform": "ucloud"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/firewall',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        print(r.json())
        print(r.request.body)
        assert r.json()['RetCode'] == expect_code


if __name__ == '__main__':
    unittest.main(verbosity=2)
