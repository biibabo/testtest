from ddt import ddt, file_data

from core.basecase import BaseCase


@ddt
class TestDisk(BaseCase):
    @file_data("../testdata/test_disk/test_disk_ucloud.json")
    def test_01_createdisk(self, OrgId, Name, expect_code):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=CreateDisk"
        data = {"AccountId": 2,
                "Platform": "ucloud",
                "OrgId": OrgId,
                "DiskInstances": [{
                    "Id": 0,
                    "Count": 1,
                    "RegionEn": "cn-sh2",
                    "ZoneEn": "cn-sh2-01",
                    "ChargeType": "Dynamic",
                    "Name": Name,
                    "Size": 20,
                    "Type": "RSSDDataDisk"
                }]}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/storage/disk',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}

        r = self.request(method="post", url=url, json=data, headers=header)
        self.assertEqual(expect_code, r.json()['RetCode'])
