import unittest

from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestVPC(BaseCase):
    @file_data("../../testdata/test_vpc/test_vpc_ucloud.json")
    def test_01_createucloudvpc(self, VPCInfo, expect_code):
        global subnetid
        global vpcid
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateVPC"
        data = {
            "AccountId": 2,
            "OrgId": 1,
            "Platform": "ucloud",
            "VPCInfo": VPCInfo}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/vpc',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        # print(r.request.body)
        print("{:-^100s}".format("Split Line"))
        # print(r.json())
        self.assertEqual(expect_code, r.json()['RetCode'])
        # assert r.json()['RetCode'] == expect_code
        subnetid = r.json()["Data"]["SubnetId"]
        vpcid = r.json()["Data"]["ResourceId"]

    def test_02_delsubnet(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=DeleteSubnet"
        data = {"SubnetInfo": [{"AccountId": 2, "Platform": "ucloud", "ProjectId": "org-uzao3s", "RegionEn": "cn-bj2",
                                "ResourceId": subnetid, "VPCId": vpcid}]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/subnet',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        print(r.json())

    def test_03_delvpc(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=DeleteVPC"
        data = {"VPCInfo": [{"AccountId": 2, "Platform": "ucloud", "ProjectId": "org-uzao3s", "RegionEn": "cn-bj2",
                             "ResourceId": vpcid}]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/network/vpc',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        print(r.json())


if __name__ == '__main__':
    unittest.main(verbosity=2)
