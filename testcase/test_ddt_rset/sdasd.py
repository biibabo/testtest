# -*- coding: UTF-8 -*-
from core.basecase import BaseCase


class TestCreatevm(BaseCase):
    def test_01_GetResourceDetail(self):
        url = 'https://cmp-fe.ucloud.cn/api/gateway?Action=GetResourceDetail'
        data = {"cmpUuid": "2.ucloud.uhost-e15yw2v1uka", "ResourceType": "vm"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        self.Status = r.json()['Data']['Status']
        print(r.json())
    def test_02_ChangeVMConfig(self):
        self.test_01_GetResourceDetail()
        print(self.Status)

    def test_03_ChangeVMConfig(self):
        # 4关机，2运行中
        self.test_01_GetResourceDetail()
        Status = self.Status
        print(Status)
        if Status == 4:
            # cmpUuids = globals()['cmpUuids']
            # cmpUuid = ''.join(cmpUuids)
            url = "https://cmp-fe.ucloud.cn/api/gateway?Action=ChangeVMConfig"
            data = {"AccountId":2,
                    "Platform":"ucloud",
                    "ProjectId":"org-uzao3s",
                    "RegionEn":"cn-sh2",
                    "cmpUuid":"2.ucloud.uhost-e15yw2v1uka",
                    "CPU":2,
                    "Memory":4,
                    "Disks":
                        [{"Id":"bsi-9a236c13",
                          "Type":26,
                          "Size":30,
                          "DiskUsage":"SystemDisk",
                          "Platform":"ucloud",
                          "DatastoreResourceId":""},
                         {"Id":"bsr-e16s4mirflc",
                          "Type":5,"Size":30,"DiskUsage":"DataDisk","Platform":"ucloud","DatastoreResourceId":""}],
                    "EIP":[{"Id":"eip-e16s4zk9cn3","Ip":"106.75.240.12","Bandwidth":2,"Type":"Bgp"}]}
            header = {
                'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm',
                'Origin': 'https://cmp-fe.ucloud.cn',
                'Cookie': self.cookie}
            r = self.request(method="post", url=url, json=data, headers=header)
            self.assertEqual(0, r.json()['RetCode'])
            print(r.json()["Data"]["UpdateDiskRes"][0]['Id'])
            print(r.json()["Data"]["UpdateDiskRes"][1]['Id'])

        elif Status == 2:
            # self.test_03_StopVM()
            print("关机中")
            self.test_01_GetResourceDetail()
            Status = self.Status
            if Status == 4:
                self.test_03_ChangeVMConfig()
            else:
                self.test_01_GetResourceDetail()
        else:
            print("此状态暂不支持改配")



