# -*- coding: UTF-8 -*-
import logging
import time

import polling as polling
import requests
from ddt import ddt, file_data

from core.basecase import BaseCase


# @ddt
class TestCreatevm(BaseCase):
    global SerialNum

    # @file_data("../../testdata/test_vm/test_vm_ucloud.json")
    # 创建ucloud云主机
    # def test_01_WorkflowCreateVM(self):
    #     global SerialNum
    #     url = "https://cmp-fe.ucloud.cn/api/gateway?Action=WorkflowCreateVM"
    #     data = {
    #         "AccountId": 2,
    #         "OrgId": 1,
    #         "Platform": "ucloud",
    #         "PlatformId": 1,
    #         "AccountName": "混合云正式账号",
    #         "VMInstances": [
    #             {
    #                 "Id": 1672803465100,
    #                 "Name": "UHost",
    #                 "Count": 1,
    #                 "RegionEn": "cn-sh2",
    #                 "ZoneEn": "cn-sh2-01",
    #                 "MachineType": "OM",
    #                 "GPUType": "",
    #                 "CPUPlatform": "Intel/Auto",
    #                 "GPU": 0,
    #                 "CPU": 1,
    #                 "Memory": 2,
    #                 "Password": "VWNsb3VkQDEyMw==",
    #                 "ImageId": "uimage-32hxo4",
    #                 "Flavor": {
    #                     "Id": "66689fd4-65de-4064-9f17-d8d6123da2bd",
    #                     "Disk": 0,
    #                     "RAM": 2048,
    #                     "Name": "快杰共享型",
    #                     "VCPUs": 1,
    #                     "CPUName": "",
    #                     "MaxDataDiskCount": 0,
    #                     "MachineType": "OM",
    #                     "GPUType": "",
    #                     "GPU": 0,
    #                     "CPUPlatformId": "Intel/Auto",
    #                     "CPUPlatformName": "Intel"
    #                 },
    #                 "BootDiskType": "CLOUD_RSSD",
    #                 "BootDiskSize": 20,
    #                 "Disks": [
    #                     {
    #                         "Type": "CLOUD_RSSD",
    #                         "Size": 20
    #                     }
    #                 ],
    #                 "VPCId": "uvnet-ivop2ysg",
    #                 "SubnetId": "subnet-s2q42du5",
    #                 "WANSGId": "firewall-oij5dter",
    #                 "CreateEIP": True,
    #                 "ChargeType": "Dynamic",
    #                 "OperatorName": "Bgp",
    #                 "EIPPayMode": "Traffic",
    #                 "EIPBandwidth": 1
    #             }
    #         ]
    #     }
    #     header = {
    #         'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm/create',
    #         'Origin': 'https://cmp-fe.ucloud.cn',
    #         'Cookie': self.cookie}
    #
    #     r = self.request(method="post", url=url, json=data, headers=header)
    #     # self.assertEqual(expect_code, r.json()['RetCode'])
    #     SerialNum = r.json()["Data"]["SerialNum"]
    #     print(SerialNum, 'SerialNum=====')

    # 获取流程状态

    def test_02_GetWorkflowInstProcess(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=GetWorkflowInstProcess"
        data = {"SerialNum": "CMPE5D2131F97BD47AD88729E3FBEDE5A31"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm/create',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        # startTime = time.time()
        while True:
            r = self.request(method="post", url=url, json=data, headers=header)
            if r.json()["Data"]["Nodes"] == [] or r.json()["Data"]["Nodes"][-1]["NodeCode"] != "end_node":
                continue
            elif r.json()["Data"]["Nodes"][-1]["NodeCode"] == "end_node" and \
                    r.json()["Data"]["Nodes"][-1]["NodeStatus"] == 2:
                print("创建成功并绑定到组织")
                break
            else:
                print('查询异常')
        print("--------------", r.json()["Data"]["Nodes"][-1]["NodeTitle"])
        cmpUuids = r.json()["Data"]["Nodes"][-1]["Context"]["CreateVMResponse"]["ResourceIds"]
        globals()['cmpUuids'] = cmpUuids
        # print(type(cmpUuids))
        # cmpUuid = ''.join(cmpUuids)
        # print(cmpUuid)
        # print(type(cmpUuid))
        # ResourceId = cmpUuid[9:]
        # print(ResourceId)

    # 关机
    def test_02_StopVM(self):
        url = "https://cmp-fe.ucloud.cn/api/gateway?Action=StopVM"
        data = {"ResourceIds": "cmpUuids"}
        header = {
            'Referer': 'https://cmp-fe.ucloud.cn/cloud-fe/resource/vm/create',
            'Origin': 'https://cmp-fe.ucloud.cn',
            'Cookie': self.cookie}
        r = self.request(method="post", url=url, json=data, headers=header)
        print(r.json()["Data"]["ResourceIds"])

# 开机
# 重启
# 改配
# 重置密码
# 制作镜像
# 删除云主机
